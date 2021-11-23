"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
"""
from collections import Counter

import requests
from bs4 import BeautifulSoup


def count_dots_on_i(url: str) -> int:
    try:
        # scrape raw site
        website = requests.get(url)
        # scrape site
        all_chars = Counter(str(website.content))
        return all_chars['i']
    except requests.exceptions.RequestException:
        raise ValueError(f"Unreachable {url}")
