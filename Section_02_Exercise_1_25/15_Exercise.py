"""
Exercise No. 15

Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c
from the range a, b inclusive.

Example:
    evenly_divisible(1, 10, 20) -> 20
    # No number between 1 and 10 can evenly divided by 20.

    evenly_divisible(1, 10, 2) -> 30
    # 2 + 4 + 6 + 8 + 10 = 30

    evenly_divisible(1, 10, 3) -> 18
    # 3 + 6 + 9 = 18

Notes:
    Return 0 if three is no number between a and b that can be evenly divided by c.
"""


def even_divisible(a, b, c):
    return sum(i for i in range(a, b + 1) if not i % c)


print(even_divisible(1, 10, 3))
