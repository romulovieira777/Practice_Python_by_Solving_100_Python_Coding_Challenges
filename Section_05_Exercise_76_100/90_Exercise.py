"""
Exercise No. 90

The Farey sequence of order n is the set of all fractions with a denominator between 1 and n, reduced and returned in
ascending order. Given n, return the Farey sequence as a list, with each fraction being represented by a string in the
form "numerator/denominator".

Examples:
    farey(1) -> ['0/1', '1/1']

    farey(4) -> ['0/1', '1/4', '1/3', '1/2', '2/3', '3/4', '1/1']

    farey(5) -> ['0/1', '1/5', '1/4', '1/3', '2/5', '1/2', '3/5', '2/3', '3/4', '4/5', '1/1']

Notes:
    - The Farey sequence will always begin with "0/1" and end with "1/1".
"""
from fractions import Fraction


def farey(n):
    r = range(1, n + 1)
    a = sorted(set(Fraction(i, j) for i in r for j in r if i < j))
    return ['0/1'] + list(map(str, a)) + ['1/1']


print(farey(5))
