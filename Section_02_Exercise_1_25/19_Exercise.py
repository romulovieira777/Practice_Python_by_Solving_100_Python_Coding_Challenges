"""
Exercise No. 19

You're in the midst of creating a typing game.

Create a function that takes in two lists: the list of user-typed words, and the list of correctly-typed words and
outputs a list containing 1 s (correctly-typed words) and -1 s (incorrectly-typed words).

# Inputs:

User-typed words: ["cat", "blue", "skt", "umbrells", "paddy"]
Correct: ["cat", "blue", "sky", "umbrella", "paddy"]

# Outputs: [1, 1, -1, -1, 1]

Examples:
    correct_stream(
        ["it", "is", "find"],
        ["it", "is", "fine"]
    ) -> [1, 1, -1]

    correct_stream(
        ["april", "showrs", "bring", "may", "flowers"],
        ["april", "showers", "bring", "may", "flowers"]
    ) -> [1, -1, 1, 1, 1]

Notes:
    The input list lengths will always be the same.
"""


def correct_stream(user, correct):
    return [1 if user[i] == correct[i] else -1 for i in range(len(user))]
