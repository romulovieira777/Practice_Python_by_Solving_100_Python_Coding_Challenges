"""
Exercise No. 87

- Given a dictionary containing up to six phrases, return a list containing the matching phrases according to the given
string (p).
- Ignore any digit that is placed after or before the given string.
- Whether the first letter is capitalized or not, if all letters of the word match the given string (p), it is valid.
- If it does not match the given string (p) then None.

Examples:
    find_pattern({
        "Phrase_01": "CCOVIDD-19 is no goog",
        "Phrase_02": "COVID-18 is no good",
        "Phrase_03": "COVID-17 is no good"
    }, "COVID-19") -> ['Phrase_01 = None', 'Phrase_02 = None', 'Phrase_03 = None']

    find_pattern({
        "Phrase_01": "Edabit is great",
        "Phrase_02": "Edabit is very great",
        "Phrase_03": "Edabit is really great"
    }, "really") -> ['Phrase_01 = None', 'Phrase_02 = None', 'Phrase_03 = really']
"""
from re import search, IGNORECASE


def find_pattern(dict_, p):
    return sorted("{} = {}".format(k, p if search(p, v, IGNORECASE) else None) for k, v in dict_.items())


print(find_pattern({
        "Phrase_01": "Edabit is great",
        "Phrase_02": "Edabit is very great",
        "Phrase_03": "Edabit is really great"
    }, "really"))
