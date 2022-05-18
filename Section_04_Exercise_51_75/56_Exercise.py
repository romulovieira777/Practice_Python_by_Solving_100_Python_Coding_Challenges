"""
Exercise No. 56

Create a function that determines whether a string is a valid hex code.

A hex code from A-F. All alphabetic characters may be uppercase or lowercase.

Examples:
    is_valid_hex_code("#CD5C5C") -> True

    is_valid_hex_code("#EAECEE") -> True

    is_valid_hex_code("#eaecee") -> True

    is_valid_hex_code("#CD5C58C") -> False
    # Length exceeds 6

    is_valid_hex_code("#CD5C5Z") -> False
    # Not all alphabetic characters in A-F

    is_valid_hex_code("#CD5C&C") -> False
    # Contains unacceptable character

    is_valid_hex_code("CD5C5C") -> False
    # Missing #
"""
import re


def is_valid_hex_code(txt):
    return bool(re.match(r'#[A-Fa-f0-9]{6}$', txt))


print(is_valid_hex_code("#eaecee"))
