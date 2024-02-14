x = ["apple", "banana"]
y = ["apple", "banana"]

z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y