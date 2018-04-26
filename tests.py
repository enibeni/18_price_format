import unittest
from format_price import format_price


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

    def test_should_format_number_with_a_minor_float_part(self):
        price = 3245.0000001
        expected = "3 245"
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

    def test_should_format_number_with_too_big_precision(self):
        price = 1234.565656
        expected = "1 234.57"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_add_zero_to_precision(self):
        price = 1234.5
        expected = "1 234.50"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_format_string(self):
        price = "1234567890.01"
        expected = "1 234 567 890.01"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_format_negative_number(self):
        price = -1234.99
        expected = "-1 234.99"
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_return_none_for_incorrect_symbols(self):
        price = "!.@#"
        expected = None
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_return_none_for_double_float_part(self):
        price = "123.56.78"
        expected = None
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

    def test_should_return_none_for_letters(self):
        price = "one hundred twenty three"
        expected = None
        formatted_price = format_price(price)
        self.assertEqual(expected, formatted_price)

if __name__ == "__main__":
    unittest.main()








