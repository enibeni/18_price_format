import re
import argparse


def format_price(price):
    if not re.match(r"^\d+\.?\d*$", str(price)):
        raise ValueError(
            "Wrong input, expected number, but {} was given".format(price)
        )
    price = float(price)
    if price.is_integer():
        format_string = ",.0f"
    else:
        format_string = ",.2f"
    return format(price, format_string).replace(",", " ")


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
    print(format_price(args.price))
