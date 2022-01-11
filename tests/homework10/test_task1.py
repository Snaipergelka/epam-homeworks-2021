import asyncio
import re

import aiohttp
from aioresponses import aioresponses

from homework10.task1 import get_load_return_all_data


def test_request():
    """
        Testing that main function parses all the required info
        and saves in array of dicts.
    """
    loop = asyncio.get_event_loop()
    aiohttp.ClientSession()

    cbr_pattern = re.compile(r'^http://www.cbr.ru/scripts.*$')

    sp_pattern = re.compile(
        r"^https://markets.businessinsider.com/index/components/s&p_500.*$")

    company_pattern = re.compile(
        r"^https://markets.businessinsider.com/stocks/.*$")

    with aioresponses(status=243) as m:
        cbr_text = """<Valute ID="R01215">
                      <NumCode>208</NumCode>
                      <CharCode>DKK</CharCode>
                      <Nominal>1</Nominal>
                      <Name>Датская крона</Name>
                      <Value>11,1939</Value>
                      </Valute>
                      <Valute ID="R01235">
                      <NumCode>840</NumCode>
                      <CharCode>USD</CharCode>
                      <Nominal>1</Nominal>
                      <Name>Доллар США</Name>
                      <Value>75,1315</Value>
                      </Valute>"""
        m.get(cbr_pattern, body=cbr_text)

        m.get(sp_pattern, body=str(
            open("tests/homework10/html.txt").read()), repeat=True)

        m.get(company_pattern, body=str(
            open("tests/homework10/html.txt").read()), repeat=True)

        resp = loop.run_until_complete(
            get_load_return_all_data(
                "https://markets.businessinsider.com/index/components/s&p_500")
        )

    assert resp == [
        {
            'price': 10129.980145000001,
            'code_name': 'ABBV',
            'p_e': 9.91,
            'income': 32.84549651311266,
            'name': 'AbbVie Inc',
            'one_year_result': 27.87
        },
        {
            'price': 10129.980145000001,
            'code_name': 'ABBV',
            'p_e': 9.91,
            'income': 32.84549651311266,
            'name': 'Arthur J. Gallagher & Co.',
            'one_year_result': 34.36
        }
    ]
