"""
Exercise No. 32

Return the total number of lists inside a given list.

Examples:
    num_of_sublists([[1, 2, 3]]) -> 1

    num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) -> 3

    num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) -> 4

    num_of_sublists([1, 2, 3]) -> 0
"""


def num_of_sublists(lst):
    return sum(1 for i in lst if type(i) == list)


print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
