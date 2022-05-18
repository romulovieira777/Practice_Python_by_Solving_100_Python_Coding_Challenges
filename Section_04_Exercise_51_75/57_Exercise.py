"""
Exercise No. 57

Create a function that takes a string containing integers as well as other characters and return the sum of the negative
integer only.

Examples:
    negative_sum("-12 13%148-11") -> -23
    # -12 + -11 = -23

    negative_sum("22 13%148-11-22 13 12") -> -33
    # -11 + -22 = -33

Notes:
    - There is at least one negative integer.
"""
import re


def negative_sum(chars):
    negative_sum = lambda s: sum(map(int, re.findall('-\d+', s)))
    return negative_sum


print(negative_sum("22 13%148-11-22 13 12"))
