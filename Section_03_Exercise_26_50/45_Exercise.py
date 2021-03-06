"""
Exercise No. 45

Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces
are included. If there are no duplicates, return 0.

Example:
    duplicates("Hello World!") -> 3
    # "o" = 2, "l" = 3.
    # "o" is duplicated 1 extra time and "l" duplicated 2 extra times.
    # Hence 1 + 2 = 3

    duplicates("foobar") -> 1

    duplicates("helicopter") -> 1

    duplicates("birthday") -> 0
    " if there are no duplicates, return 0.

Notes:
    Makes sure to only start counting the second time a character appears.
"""


def duplicates(txt):
    return len(txt) - len(set(txt))


print(duplicates("Hello World!"))
