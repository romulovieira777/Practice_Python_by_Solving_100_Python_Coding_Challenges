"""
Exercise No. 89

Write a function that will return True if a given string (divided and grouped into a size) will contain a set of
consecutive numbers (regardless of orientation: whether ascending or descending), otherwise, return False.

Examples:
    is_consecutive("121314151617") -> True
    # Contains a set of consecutive ascending numbers.
    # If grouped into 2's : 12, 13, 14, 15, 16, 17

    is_consecutive("123124125") -> True
    # Contains a set of consecutive ascending numbers.
    # If grouped into 3's : 123, 124, 125

    is_consecutive("32332432536") -> False
    # Regardless of the grouping size, the numbers can't be consecutive.

    is_consecutive("326325324323") -> True
    # Contains a set of consecutive descending numbers.
    # If grouped into 3's : 326, 325, 324, 323

    is_consecutive("667666") -> True
    # Consecutive descending numbers: 667 and 666.

    is_consecutive("99989795493") -> False

Notes:
    - A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string
    has at least two of them.
"""
from re import findall


def is_consecutive(s):
    for k in range(1, len(s) // 2 + 1):
        n = list(map(int, findall(r'.{1,' + str(k) + '}', s)))
        if all(b - a == 1 for a, b in zip(n, n[1:])) or all(b - a == -1 for a, b in zip(n, n[1:])): return True
    return False


print(is_consecutive("99989795493"))
