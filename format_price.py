import re
import argparse


def format_price(price):
    precision = 2
    price = str(price)
    if re.match(r"^\d+([.,])?\d*$", price):
        price = price.replace(",", ".")
        if float(price).is_integer():
            format_string = ",.0f"
        else:
            float_part = price.split(".")[1]
            if len(float_part) > precision:
                unwanted_precision = len(float_part) - precision
                price = price[:-unwanted_precision]
            if price[-precision:] == "00":
                format_string = ",.0f"
            else:
                format_string = ",.2f"
        return format(float(price), format_string).replace(",", " ")


def get_input_argument_parser():
    parser = argparse.ArgumentParser("Format price")
    parser.add_argument(
        "-p",
        "--price",
        required=True,
        help="Price to format"
    )
    return parser


if __name__ == "__main__":
    parser = get_input_argument_parser()
    args = parser.parse_args()
    formatted_price = format_price(args.price)
    if not formatted_price:
        raise ValueError(
            "Wrong input, expected number, "
            "but {} was given".format(args.price)
        )
    print(formatted_price)
