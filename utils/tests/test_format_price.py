from django.test import TestCase
from utils.numbers.format_price import format_price


class FormatPriceTest(TestCase):
    def test_format_price_return_a_formated_price(self) -> None:
        f_price_1 = format_price(123456)
        f_price_2 = format_price(123456.48)
        f_price_3 = format_price(1250.968)
        self.assertEqual(f_price_1, '123456,00')
        self.assertEqual(f_price_2, '123456,48')
        self.assertEqual(f_price_3, '1250,97')
