"""
Exercise No. 71

Give a list of math equations (give as strings), return the percentage of correct answers as a string. Round to the
nearest whole number.

Examples:
    mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]) ->"75%"

    mark_maths(["1-2=-2"]) -> "0%"

    mark_maths(["2+3=5", "4+4=9", "3-1=2"]) -> "67%"

Notes:
    - You can expect only addition and subtraction.
    - Note how there aren't any spaces in any given equation.
"""


def mark_maths(lst):
    lst = [eval(i.replace('=', '==')) for i in lst]
    return str(round(100 * sum(lst) / len(lst))) + '%'


print(mark_maths(["2+3=5", "4+4=9", "3-1=2"]))
