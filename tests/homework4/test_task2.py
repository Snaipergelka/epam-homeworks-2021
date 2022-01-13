"""
Test should use Mock instead of real network interactions.
"""
from unittest import TestCase
from unittest.mock import Mock, patch

from homework4.task2 import count_dots_on_i


class TestCountDots(TestCase):

    def test_count_dots_on_i(self):
        """
            Testing that function counts dots on i by imitating
            get request from website instead of real network interactions.
        """

        mock_get_patcher = patch('homework4.task2.requests.get')
        mock_get = mock_get_patcher.start()

        html_str = str(open("tests/homework4/html_website.txt").readlines())
        result = 59

        mock_get.return_value = Mock(status_code=200, content=html_str)

        url = 'https://docs.python.org/3/library/unittest.mock.html'
        response = count_dots_on_i(url=url)

        mock_get_patcher.stop()

        self.assertEqual(response, result)
