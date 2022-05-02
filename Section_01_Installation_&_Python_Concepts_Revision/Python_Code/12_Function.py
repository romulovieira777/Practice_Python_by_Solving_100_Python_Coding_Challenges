def sumOfNumbers(a, b):
    return a + b


print(sumOfNumbers(3, 4))

sumOfNumbers_02 = lambda a, b: a + b

print(sumOfNumbers_02(10, 5))


def name(a):
    print(a)


name("Arrow")


class Person:
    def __init__(self, fname, lname):
        self.fname =fname
        self.lname = lname


p1 = Person("Arrow", "Arqueiro")

print(p1.fname)
print(p1.lname)
