"""
Exercise No. 12

Create a function that takes a list and returns the difference between the biggest and the smallest numbers.

Examples
    difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) -> 82
    # Smallest number is -50, biggest number is 32.

    difference_max_min([44, 32, 86, 19])-> 67
    # Smallest number is 19, biggest number is 86.
"""


def difference_max_min(lst):
    return max(lst) - min(lst)


print(difference_max_min([-50, 30, 80, 250]))
