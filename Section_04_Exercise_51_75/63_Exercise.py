"""
Exercise No. 63

Given a list of integers, return the smallest positive integer not present in the list.

Here is a representative example. Consider the list:
    [-2, 6, 4, 5, 7, -1, 7, 1, 3, 6, 6, -2, 9, 10, 2, 2]
After reordering, the list becomes:
    [-2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 7, 9, 10]
... from which we see that the smallest missing positive integer is 8.

Examples:
    min_miss_pos([-2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2]) -> 8
    # After sorting, list becomes [-2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 9, 10]
    # So the smallest missing positive integer is 8

    min_miss_pos([5, 9, -2, 0, 1, 3, 9, 3, 8, 9]) -> 2
    # After sorting, list becomes [-2, 0, 1, 3, 3, 5, 8, 9, 9, 9]
    #So the smallest missing positive integer is 2

    min_miss_pos([0, 4, 4, -1, 9, 4, 5, 2, 10, 7, 6, 3, 10, 9]) -> 1
    # After sorting, list becomes [-1, 0, 2, 3, 4, 4, 4, 5, 6, 7, 9, 9, 10, 10]
    # So the smallest missing positive integer is 1

Notes:
    For the sake of clarity, recall that 0 is not considered to be a positive number.
"""


def min_miss_pos(lst):
    i = 1
    while True:
        if not i in lst:
            return i
        i += 1
    return i


print(min_miss_pos([-2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2]))
