from unittest import TestCase
from utils.string.format_string import format_string_into_list


class FormatStringTests(TestCase):
    def test_format_string_return_a_list_of_strings_formated(self) -> None:
        list_string = format_string_into_list(
            '127.0.0.1, *, https://www.mywebsite.com, localhost',
            default='127.0.0.1, *, https://www.mywebsite.com, localhost'
        )
        self.assertEqual(
            list_string,
            ['127.0.0.1', '*', 'https://www.mywebsite.com', 'localhost']
        )
