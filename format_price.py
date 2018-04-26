import re
import argparse


def format_price(price):
    precision = 2
    if re.match(r"^-?\d+\.?\d*$", str(price)):
        price = round(float(price), precision)
        if str(price)[-1:] == "0":
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
