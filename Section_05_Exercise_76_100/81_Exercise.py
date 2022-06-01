"""
Exercise No. 81

Create a function that takes a list of numbers or strings and returns a list with the items from the original list
stored into sublist. Items of the same value should be in the same sublist.

Examples:
    advanced_sort([2, 1, 2, 1]) -> [[1, 1], [2, 2]]

    advanced_sort([5, 4, 5, 5, 4, 3]) -> [[3], [4, 4], [5, 5, 5]]

    advanced_sort(["b", "a", "b", "a", "c"]) -> [['a', 'a'], ['b', 'b'], ['c']]

Notes:
    - The sublist should be returned to the order of each element's first appearance in the given list.
"""


def advanced_sort(lst):
    return [[i] * lst.count(i) for i in sorted(set(lst), key=lst.index)]


print(advanced_sort(["b", "a", "b", "a", "c"]))
