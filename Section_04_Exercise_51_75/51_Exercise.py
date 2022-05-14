"""
Exercise No. 51

Write a recursive function that will return the longest word in a sentence. In cases where more than one word is found,
return the first one.

Examples:
    find_longest("") ->

    find_longest("A thing of beauty is a joy forever.") -> forever

    find_longest("") ->

    find_longest("") ->

Notes:
    - Special characters and symbols don't count as part of the word.
    - Return the longest word found in lowercase letters.
    - You are expected to solve this challenge via a recursive approach.
"""
import re


def find_longest(setence):
    return max(re.split('\W', setence.lower()), key=len)


print(find_longest("A thing of beauty is a joy forever."))
