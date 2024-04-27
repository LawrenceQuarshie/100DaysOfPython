fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []
for i in range(len(fruits)):
    if "a" in fruits[i]:
        newlist.append(fruits[i])

print(newlist)