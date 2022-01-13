import asyncio
import re
from unittest.mock import Mock, patch

import aiohttp
from aioresponses import aioresponses

from homework10.task1 import BusinessInsiderParser


def test_request():
    """
        Testing that main function parses all the required info
        and saves in array of dicts.
    """
    loop = asyncio.get_event_loop()
    test_instance = BusinessInsiderParser(session=aiohttp.ClientSession())

    sp_pattern = re.compile(
        r"^https://markets.businessinsider.com/index/components/s&p_500.*$")

    company_pattern = re.compile(
        r"^https://markets.businessinsider.com/stocks/.*$")

    mock_get_patcher = patch('homework10.task1.requests.get')
    mock_get = mock_get_patcher.start()
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
                          <Value>75,1</Value>
                          </Valute>"""
    mock_get.return_value = Mock(status_code=200, text=cbr_text)

    with aioresponses(status=200) as m:

        m.get(sp_pattern, body=str(
            open("tests/homework10/html.txt").read()), repeat=True)

        m.get(company_pattern, body=str(
            open("tests/homework10/html.txt").read()), repeat=True)

        resp = loop.run_until_complete(
            test_instance.get_load_return_all_data(
                "https://markets.businessinsider.com/index/components/s&p_500")
        )
    mock_get_patcher.stop()

    assert resp == [
        {
            'price': 10125.733,
            'code_name': 'ABBV',
            'p_e': 9.91,
            'income': 32.84549651311266,
            'name': 'AbbVie Inc',
            'one_year_result': 27.87
        },
        {
            'price': 10125.733,
            'code_name': 'ABBV',
            'p_e': 9.91,
            'income': 32.84549651311266,
            'name': 'Arthur J. Gallagher & Co.',
            'one_year_result': 34.36
        }
    ]
