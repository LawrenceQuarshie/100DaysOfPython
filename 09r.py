def myfunction(**myvar):
    print(type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

myfunction(name = "Tobias", age = 30, city = "Bergen")