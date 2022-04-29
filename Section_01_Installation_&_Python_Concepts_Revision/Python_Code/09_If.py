a = 10
b = 9

if a > b:
    print("a is greater than b")
else:
    print("b is greater")


print("a is greater than b") if a > b else print("b is greater")


print("a is greater than b") if (a > b) else print("b is greater") if (a > b) else print("Both are equal")


if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater")
else:
    print("Both are equal")
