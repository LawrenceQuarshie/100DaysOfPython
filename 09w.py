def myfunction(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

myfunction("User Info", "Emil", "Tobias", age = 25, city = "Oslo")