import asyncio
import json
import logging
from concurrent.futures import ProcessPoolExecutor
from itertools import zip_longest
from math import inf
from typing import Dict, Optional

import aiohttp
import aiohttp_retry
import requests
from bs4 import BeautifulSoup


async def get_text_website(website_url, session) -> Optional[str]:
    """
        Get text content of website.
    """
    async with session.get(website_url) as resp:
        try:
            response = await resp.text()
        except aiohttp.ClientError as e:
            response = None
            logging.error(f"Exception occurred when making "
                          f"request to {website_url}."
                          f" Error type: {e.__name__}")
        finally:
            return response


def make_soup(response) -> BeautifulSoup:
    """
        Parse html of the website.
    """
    soup = BeautifulSoup(response, "html.parser")
    return soup


def get_company_names_urls(website_html) -> Dict[str, str]:
    """
        Parse company names and company websites urls from main table.
    """
    company_names_urls_dict = {}
    company_names = (x.text.strip()
                     for x in website_html.findAll(
            "td", {"class": "table__td table__td--big"}))

    for company_name in company_names:
        tag = website_html.find("a", href=True, title=company_name)
        company_names_urls_dict[company_name] = \
            'https://markets.businessinsider.com' + tag['href']
    return company_names_urls_dict


def grouper(iterable, n, fillvalue=None):
    """
    Collect data into non-overlapping fixed-length chunks or blocks
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def get_one_year_statistic(website_html):
    """
        Parse company names and company one year income/loss from main table.
    """
    raw_table_content = website_html.findAll("td", {"class": "table__td"})

    table_content = (
        (
            row[0].text.strip(),
            float(row[7].text.strip().split('\n')[1].strip('%'))
        )
        for row in grouper(raw_table_content, 8, None))

    return dict(table_content)


def all_next_pages_urls(website_html):
    """
        Parse all pages urls from main website.
    """
    pages = website_html.find("div",
                              {"class": "finando_paging margin-top--small"})
    pages = str(pages).split("|")
    pages_url = [
        f'https://markets.businessinsider.com/index/components/s&p_500?p={i}'
        for i in range(1, len(pages) + 1)]
    return pages_url


def get_price(company_website_html):
    """
        Parse price of the stocks from company website.
    """
    price = company_website_html.find("span",
                                      {"class":
                                       "price-section__current-value"})
    return float(price.text.replace(',', '')) if price else None


def get_value_exchange():
    """
        Parse exchange value from central bank website.
    """
    cbr_url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    try:
        website_html_raw = requests.get(cbr_url)
    except requests.exceptions.RequestException as e:
        logging.error(f"Exception occurred when making "
                      f"request to {cbr_url}. "
                      f"Error type: {e.__name__}")
        return None

    website_html = website_html_raw.text.split('<Valute ID=')
    result = [x.strip("</Value></Valute>").split("<Value>")
              for x in website_html if "R01235" in x][0][1].replace(',', '.')

    return float(result)


def get_price_in_rub(exchange_value, price):
    """
        Calculate price of stocks in rubles.
    """
    if not price or not exchange_value:
        return float('-inf')
    return exchange_value * price


def get_code_name(company_website_html):
    """
        Parse code name of company from company card website.
    """
    code_name = company_website_html.find("span",
                                          {"class": "price-section__category"})
    return code_name.text.strip().strip("Stock , ") if code_name else None


def get_p_e(company_website_html):
    """
        Parse price to earnings from company card website.
    """
    p_e_value_list = company_website_html.findAll("div",
                                                  {"class":
                                                   "snapshot__data-item"})
    if not p_e_value_list:
        return float('inf')
    p_e_value = [x.text.split() for x in p_e_value_list
                 if "P/E Ratio" in x.text]
    if not p_e_value:
        return float('inf')
    return float(p_e_value[0][0].replace(',', ''))


def get_52_weeks_low(company_website_html):
    """
        Parse 52 weeks low price stock result from company card website.
    """
    weeks_low = [x.text.strip().split() for x in
                 company_website_html.findAll(
                     "div",
                     {"class":
                      "snapshot__data-item snapshot__data-item--small"}
                 )]
    if not weeks_low or not any("Week" in sublist for sublist in weeks_low):
        return None
    if len(weeks_low) < 2:
        return float(weeks_low[0][0].replace(',', ''))
    return float(weeks_low[1][0].replace(',', ''))


def get_52_weeks_high(company_website_html):
    """
        Parse 52 weeks high price stock result from company card website.
    """
    weeks_high = [x.text.strip().split() for x in
                  company_website_html.findAll(
                      "div",
                      {"class":
                       "snapshot__data-item snapshot__data-item--small"
                       " snapshot__data-item--right"}
                  )]
    if not weeks_high or not any("Week" in sublist for sublist in weeks_high):
        return None
    if len(weeks_high) < 2:
        return float(weeks_high[0][0].replace(',', ''))
    return float(weeks_high[1][0].replace(',', ''))


def weeks_high_low_income(weeks_high, weeks_low):
    """
        Calculating income if stocks were bought on 52 weeks low and sold
        on 52 weeks high.
    """
    if weeks_high is None or weeks_low is None:
        return float(-inf)
    return ((weeks_high - weeks_low) / weeks_low) * 100


async def get_load_return_all_data(first_page_website_url):
    """
        This function:
        1. Using asyncio and aiohttp makes parallel requests.
        2. Using parse_info_from_company_page parses all
         required information from company page.
        3. Using ProcessPoolExecutor pararllels threads
         to speed up parsing info from website htmls.
    """
    connector = aiohttp.TCPConnector(limit=50)
    async with aiohttp_retry.RetryClient(connector=connector) as session:

        logging.info('STEP 1: parsing main page with a table')
        # STEP 1: parsing main page with a table
        website_str = await get_text_website(first_page_website_url,
                                             session)
        website_html = make_soup(website_str)

        logging.info('Extract all next pages '
                     'that contain other pieces of the table')
        # extract all next pages that contain other pieces of the table
        all_next_pages_urls_list = all_next_pages_urls(website_html)

        logging.info('Extract names and urls to company description')
        # extract names and urls to company description
        all_companies_names_urls_dict = get_company_names_urls(website_html)

        logging.info('Extract names and one year statistic'
                     ' to company description')
        # extract names and one year statistic to company description
        all_companies_names_one_year_stat_dict = \
            get_one_year_statistic(website_html)

        logging.info('STEP 2: parsing other pages to build single list  '
                     'with links to all companies detailed info')
        # STEP 2: parsing other pages to build single list
        # with links to all companies detailed info
        tasks = []
        for page_url in all_next_pages_urls_list:
            tasks.append(get_text_website(page_url, session))

        logging.info('Waiting for i/o bound tasks')
        # waiting for i/o bound tasks
        pages_urls_htmls = await asyncio.gather(*tasks)

        logging.info('Parsing info from every page')

        for html in pages_urls_htmls:
            page_website_html = make_soup(html)

            all_companies_names_urls_dict.update(
                get_company_names_urls(page_website_html))

            all_companies_names_one_year_stat_dict.update(
                get_one_year_statistic(page_website_html))

        logging.info('STEP 3: parsing detailed information'
                     ' for every company from list')
        # STEP 3: parsing detailed information for every company from list
        tasks = []
        for key, value in all_companies_names_urls_dict.items():
            tasks.append(get_text_website(value, session))

        # waiting for i/o bound tasks
        company_website_strs = await asyncio.gather(*tasks)

        logging.info("Starting parsing of company cards")
        # it is computational-bound tasks
        with ProcessPoolExecutor(60) as pool:
            all_companies = pool.map(
                parse_info_from_company_page, company_website_strs)
        all_companies = list(all_companies)
        value_exchange = get_value_exchange()
        for company_page_details, stat in zip(
                all_companies,
                all_companies_names_one_year_stat_dict.items()
                                              ):
            company_page_details.update({"name": stat[0],
                                         "one_year_result": stat[1],
                                         "price":
                                         get_price_in_rub(
                                             company_page_details["price"],
                                             value_exchange)})

    return all_companies


def parse_info_from_company_page(company_website_str):
    """
        This function parse all required information from company card.
    """
    company_website_html = make_soup(company_website_str)
    price = get_price(company_website_html)
    code_name = get_code_name(company_website_html)
    p_e = get_p_e(company_website_html)
    income = weeks_high_low_income(
        get_52_weeks_high(company_website_html),
        get_52_weeks_low(company_website_html))
    return {
        "price": price,
        "code_name": code_name,
        "p_e": p_e,
        "income": income
    }


def top_10_most_expensive(all_companies_info):
    """
        Sorting and saving in json file top 10 companies
        with most expensive stocks.
    """
    with open("top_most_expensive.json", "w") as file:
        data = sorted(all_companies_info, key=lambda x: x['price'],
                      reverse=True)[:10]
        json.dump(data, file)


def top_10_lowest_p_e(all_companies_info):
    """
        Sorting and saving in json file
        top 10 companies with lowest P/E values.
    """
    with open("top_10_lowest_p_e.json", "w") as file:
        data = sorted(all_companies_info,
                      key=lambda x: x['p_e'])[:10]
        json.dump(data, file)


def top_10_one_year_change(all_companies_info):
    """
        Sorting and saving in json file
        top 10 companies with highest one year income result.
    """
    with open("top_10_one_year_change.json", "w") as file:
        data = sorted(all_companies_info,
                      key=lambda x: x['one_year_result'],
                      reverse=True)[:10]
        json.dump(data, file)


def top_10_income(all_companies_info):
    """
        Sorting and saving in json file top 10 companies with income
        that can be earned if stocks were bought on 52 weeks low and sold
        on 52 weeks high.
    """
    with open("top_10_income.json", "w") as file:
        data = sorted(all_companies_info,
                      key=lambda x: x['income'],
                      reverse=True)[:10]
        json.dump(data, file)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(get_load_return_all_data(
        'https://markets.businessinsider.com/index/components/s&p_500')
    )
    top_10_income(data)
    top_10_one_year_change(data)
    top_10_lowest_p_e(data)
    top_10_most_expensive(data)
