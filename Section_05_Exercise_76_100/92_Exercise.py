"""
Exercise No. 92

Create a function that takes two strings. The first string contains a sentence containing the letters of the second
string in a consecutive sequence but in a different order. The hidden anagram must contain all the letters, including
duplicates, from the second string in any order and must not contain any other alphabetic characters.

Write a function to find the anagram of the second string embedded somewhere in the first string. You should ignore
character case, any spaces, and punctuation marks and return the anagram as a lower case string with no spaces or
punctuation marks.

Examples:
    hidden_anagram("An old west action hero actor", "Clint Eastwood") -> "noldwestactio"
    # The sequence "n old west actio" is a perfect anagram of "Clint Eastwood".

    hidden_anagram("Mr. Mojo Rising could be a song title", "Jim Morrison") -> "mrmojorisin"
    # The sequence "Mr. Mojo Risin" ignoring the full stop, is a perfect anagram of "Jim Morrison".

    hidden_anagram("Banana? margaritas", "ANAGRAM") -> "anamarg"
    # The sequence "ana? marg" ignoring "?" is a perfect anagram of "Anagram"

    hidden_anagram("D e b90it->?$ (c)a r...d,,#~", "bad credit") -> "debitcard"
    # When all spaces, numbers and puntuation marks are removed
    # from the whole phrase, the remaining characters from the sequence
    # "Debitcard" with is a perfect anagram of "bad credit"

    hidden_anagram("Bright is the moon", "Bongo mirth") -> "noutfound"
    # The words "Bright moon" are an anagram of "bongo mirht" but they are
    # not a continuous alphabetical sequence because the words "is the" are in
    # between. Hence the negative result, "noutfound" is returned.

Notes:
    - A perfect anagram contains all the letters of the original, in any order, no more, no less.
    - If there is no hidden anagram in the sequence, return the "noutfound"
    - As in the above examples, the hidden anagram may start or finish part way through a word and/or span multiple
    words and may contain punctuation marks and other non-alpha characters.
    - Ignore character case and any embedded non-alpha characters.
    - If there is more than 1 result in a sentence, return the nearest to the beginning.
"""
import re


def hidden_anagram(text, phrase):
    text = re.sub(r'[^a-z]', '', text.lower())
    phrase = re.sub(r'[^a-z]', '', phrase.lower())

    for i in range(len(text)):
        if sorted(phrase) == sorted(text[i:i + len(phrase)]):
            return text[i:i + len(phrase)]
    return "noutfound"


print(hidden_anagram("An old west action hero actor", "Clint Eastwood"))
