"""
Exercise No. 100

Mubashir needs your help to find out number of animals hidden in a given string txt.

You are provided with an array of animals given below:
    animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog",
               "hen", "mole", "duck", "goat"]

Rules:
    - Return the maximum number of animals names. See the below example:
        txt = "goatcode"

        count_animals(txt) -> 2
        # First animal = "dog"
        # Remaining string = "atcoe"
        # Second animal = "cat"
        # count = 2 (correct)

        # If you got a "goat" first time
        # Remaining string = "code"
        # No animal will be found during next time.
        # count = 1 (wrong)

Examples:
    count_animals("goatcode") -> 2
    # "dog", "cat"

    count_animals("cockdogwdufrbir") -> 4
    # "cow", "duck", "frog", "bird"

    count_animals("dogdogdogdogdog") -> 5
"""
animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog",
               "hen", "mole", "duck", "goat"]


def count_animals(txt):
    counts = []

    def f(t, c):
        for a in animals:
            s = t
            for x in a: s = s.replace(x, "", 1)
            if len(s) + len(a) == len(t): f(s, c + 1)
        counts.append(c)
    f(txt, 0)
    return max(counts)


print(count_animals("dogdogdogdogdog"))
