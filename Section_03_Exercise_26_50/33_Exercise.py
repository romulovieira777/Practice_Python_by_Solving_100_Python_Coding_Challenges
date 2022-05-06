"""
Exercise No. 33

Build a function that creates histograms. Every bar needs to be on a new line and its length corresponds to the numbers
in the list passed as an argument. The second argument of the function represents the character that needs to be used.

    histograms(lst, char) -> str

Examples:
    histograms([1, 3, 4], "#") -> "#\n###\n####"

    #
    ###
    ####

    histograms([6, 2, 15, 3], "=") -> "======\n==\n==============\n===

    ======
    ==
    =============
    ===

    histograms([1, 10], "+") -> "+\n++++++++++"

    +
    ++++++++++

Notes:
    For better understanding try printing out the result.
"""


def histograms(lst, char):
    return "\n".join(char * i for i in lst)


print(histograms([6, 2, 15, 3], "="))
