"""
Exercise No. 40

Create a function that checks if the box is completely filled with the asterisk symbol *.

Examples:
    completely_filled([
        "#####",
        "#***#",
        "#***#",
        "#***#",
        "#####"
    ]) -> True

    completely_filled([
        "#####",
        "#* *#",
        "#***#",
        "#***#",
        "#####"
    ]) -> False

    completely_filled([
        "###",
        "#*#",
        "###"
    ]) -> True

    completely_filled([
        "##",
        "##"
    ]) -> True

Notes:
    - Box of size n <= 2 are considered automatically filled (see example #4).
    - Empty space will always be a space character (" ").
"""


def completely_filled(lst):
    return not any(' ' in i for i in lst)


print(completely_filled([
        "#####",
        "#***#",
        "#***#",
        "#***#",
        "#####"
    ]))
