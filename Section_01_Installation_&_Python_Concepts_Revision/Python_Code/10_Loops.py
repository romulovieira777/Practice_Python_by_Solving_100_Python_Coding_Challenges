a = 1

while a <= 10:
    print(a)

    a += 1


for i in range(1, 11):
    print(i)


for i in "My name is Felicity Smoke":
    print(i)


b = {'Number': 1, 'Name': 2, 'Name2': 'Felicity Smoke', 'Country': 'USA'}
for i in b:
    print(i)


for i in b.values():
    print(i)


for i in b.keys():
    print(i)


c = list(range(1, 11))

for i, j in enumerate(c):
    print(i, j)
