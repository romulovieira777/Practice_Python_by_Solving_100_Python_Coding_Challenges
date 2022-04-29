"""
Exercise No. 13

Create a function that takes a string (will be a person's first and last name) and returns a string with the first and
last name swapped.

Examples:
    name_shuff("Donald Trump") -> "Trump Donald"

    name_shuff("Rosie O'Donnell) -> "O'Donnell Rosie"

    name_shuff("Seymour Butts") -> "Butts Seymour"

Notes:
    - There will be exactly one space between the first and last name.
"""


def name_shuff(str):
    return ' '.join(reversed(str.split(' ')))


print(name_shuff("Seymour Butts"))
