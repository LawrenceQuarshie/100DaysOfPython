a = range(1500,2701)

b = []
for x in a:
    if (x % 7 == 0) and (x % 5 == 0):
        b.append(x)

print(b)