def myfunction(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
myfunction(**person)