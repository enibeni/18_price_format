import unittest
from .format_price import format_price


class FormatPriceTests(unittest.TestCase):
    def test_should_format_short_number(self):
        price = 123
        expected = "123"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_format_long_number(self):
        price = 1234567890
        expected = "1 234 567 890"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_format_number_with_float_part(self):
        price = 1234.56
        expected = "1 234.56"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_format_number_with_zero_float_part(self):
        price = 1.0000
        expected = "1"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_format_zero(self):
        price = 0
        expected = "0"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_format_string(self):
        price = "1234567890.01"
        expected = "1 234 567 890.01"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_return_error_for_incorrect_symbols(self):
        with self.assertRaises(ValueError):
            price = "!.@#"
            format_price(price)

    def test_should_return_error_for_double_float_part(self):
        with self.assertRaises(ValueError):
            price = "123.56.78"
            format_price(price)

    def test_should_return_error_for_letters(self):
        with self.assertRaises(ValueError):
            price = "one hundred twenty three"
            format_price(price)








