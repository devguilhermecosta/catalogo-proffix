from unittest import TestCase
from utils.numbers.format_number import format_phone_number


class FormatNumberTests(TestCase):
    def test_format_number_returns_a_phone_number_without_symbols(self) -> None:  # noqa: E501
        number = format_phone_number('1-2-3-4-5-6(7),8')
        number_2 = format_phone_number('%¨6&*123-4(5)6-+')
        number_3 = format_phone_number('%¨6&*123     -4(5)6-+')
        self.assertEqual(number, '12345678')
        self.assertEqual(number_2, '6123456')
        self.assertEqual(number_3, '6123456')
