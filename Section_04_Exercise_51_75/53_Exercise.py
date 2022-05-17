"""
Exercise No. 53

The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero whose
factorial is exactly dived by the number.
    kempner(6) -> 3

    1! = 1 % 6 > 0
    2! = 2 % 6 > 0
    3! = 6 % 6 === 0

    kempner(10) -> 5

    1! = 1 % 10 > 0
    2! = 2 % 10 > 0
    3! = 6 % 10 > 0
    4! = 24 % 10 > 0
    5! = 120 % 120  === 10

A Kempner Function applied to a prime will always return the prime itself.
    Kempner(2) -> 2
    kempner(5) -> 5

Give an integer n, implement a Kempner Function.

Examples:
    kempner(6) -> 3

    kempner(10) -> 5

    kempner(2) -> 2

Notes:
    - Try solving this recursively, with an approach oriented to higher-order functions.
"""


def kempner(n, i=1, total=1):
    return max(1, i - 1) if total % n == 0 else kempner(n, i + 1, total * i)


print(kempner(6))
