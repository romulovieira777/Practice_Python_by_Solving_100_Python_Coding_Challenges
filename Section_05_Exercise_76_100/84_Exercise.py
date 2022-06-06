"""
Exercise No. 84

You bought a few bunches of fruit over the weekend. Create a function that splits a bunch into singular objects inside
a list.

Examples:
    split_bunches([
        {'name': 'grapes', 'quantity': 2}
    ]) -> [
        {'name': 'grapes', 'quantity': 1},
        {'name': 'grapes', 'quantity': 1}
    ]

    split_bunches([
        {'name': 'currants', 'quantity': 1},
        {'name': 'grapes', 'quantity': 2},
        {'name': 'bananas', 'quantity': 2}
    ]) -> [
        {'name': 'currants', 'quantity': 1},
        {'name': 'grapes', 'quantity': 1},
        {'name': 'grapes', 'quantity': 1},
        {'name': 'bananas', 'quantity': 1},
        {'name': 'bananas', 'quantity': 1}
    ]


Notes:
    - The input list will never be empty.
    - Objects will always have a name and quantity over 0.
    - The returned object should have each fruit in the same order as the original.
"""


def split_bunches(bunches):
    res = []
    for fruit in bunches:
        res += [{'name': fruit['name'], 'quantity': 1}] * fruit['quantity']
    return res


print(split_bunches([
        {'name': 'currants', 'quantity': 1},
        {'name': 'grapes', 'quantity': 2},
        {'name': 'bananas', 'quantity': 2}
    ]))
