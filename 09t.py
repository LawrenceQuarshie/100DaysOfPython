def myfunction(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

myfunction("emil123", age = 25, city = "Oslo", hobby = "coding")