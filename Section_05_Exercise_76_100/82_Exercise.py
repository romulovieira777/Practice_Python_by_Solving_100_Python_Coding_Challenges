"""
Exercise No. 82

Write a function that groups a string into parentheses cluster. Each cluster should be balanced.

Examples:
    split("()()()") -> ['()', '()', '()']

    split("((()))") -> ['((()))']

    split("((()))(())()()(()())") -> ['((()))', '(())', '()', '()', '(()())']

    split("((())())(()(()()))") -> ['((())())', '(()(()()))']

Notes:
    - All inputs strings will only contain parentheses.
    - Balanced: Every opening parents ( must exist with its matching closing parens ) in the same cluster.
"""


def split(txt):
    a = []
    b = ""
    for i in txt:
        b += i
        if b.count("(") == b.count(")"):
            a.append(b)
            b = ""
    return a


print(split("((())())(()(()()))"))
