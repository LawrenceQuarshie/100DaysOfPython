fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

thislist = [x if x != "banana" else "orange" for x in fruits]

print(thislist)