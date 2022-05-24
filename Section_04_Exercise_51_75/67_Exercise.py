"""
Exercise No. 67

Create a function that takes the width, height and character and returns a picture frame as a 2D list.

Examples:
    get_frame(4, 5, "#") -> [
        ["####"],
        ["#  #"],
        ["#  #"],
        ["#  #"],
        ["####"]
    ]

    get_frame(10, 3, "*") -> [
        ["**********"],
        ["*        *"],
        ["**********"]
    ]
    # Frame is 10 characters and wide and 3 characters tall.

    get_frame(2, 5, "0") -> "invalid"
    # Frame's width is note more than 2.

Notes:
    - Remember the gap.
    - Return "invalid" if width or height is 2 or less (can't put anything inside).
"""


def get_frame(width, height, character):
    if width <= 2 or height <= 2:
        return 'invalid'
    head = character * width
    side = character + ' ' * (width - 2) + character
    return [[i] for i in [head] + [side] * (height - 2) + [head]]


print(get_frame(10, 3, "*"))
