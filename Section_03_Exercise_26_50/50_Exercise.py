"""
Exercise No. 50

Create a function that takes a string as an argument and returns the Morse code equivalent.

Example:
    econde_morse("EDABBIT CHALLENGE") -> ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

    enconde_morse("HELP ME !") -> ".... . .-.. .--.   -- .   -.-.--"

This is dictionary can be used for coding:
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
        ')': '-.--.-', '!': '-.-.--', ' ': ' ', "'": '.----.', ':': '---...'
    }

Notes:
    - Outputs should be International Morse Code, and use the standard conventions for symbols not defined inside the
      ITU recommendation (see Resource).
    - Input value can be lower or upper case.
    - Input string can have digits.
    - Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark,
      exclamation mark).
    - One space " " is expected after each character, except the last one.
"""


def encode_morse(txt):
    d = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
        ')': '-.--.-', '!': '-.-.--', ' ': ' ', "'": '.----.', ':': '---...'
         }

    return ' '.join(d[i] for i in txt.upper())


print(encode_morse("HELP ME !"))
