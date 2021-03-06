"""
Exercise No. 30

Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

Examples:
    format_date("11/12/2019") -> "20191211"

    format_date("12/31/2019") -> "20193112"

    format_date("01/15/2019") -> "20191502"

Notes:
    Return value should be a string.
"""


def format_date(date):
    m, d, y = date.split("/")
    return ''.join((y, d, m))


print(format_date("12/31/2019"))
