# Price Formatter

This module make price human readable

# Quickstart

Run this script with Python 3.x. As an required parameter -p, you should specify a price to be formatted.

Example of script launch on Linux, Python 3.5:

```bash
$ python format_price.py -p 3245.000000
3 245
```

Adding to your project:
```python
from format_price import format_price
formatted_price = format_price(price)
```

# How to start tests
```bash
$ python -m unittest tests.py
..............
----------------------------------------------------------------------
Ran 14 tests in 0.003s
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
