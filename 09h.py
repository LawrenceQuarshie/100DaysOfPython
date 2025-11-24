def myfunction(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

myfunction("Emil", "Tobias", "Linus")