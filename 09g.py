def myfunction(*storageoptions):
    print("Smallest storage option is", storageoptions[0])

myfunction("64GB", "128GB", "256GB")
myfunction("128GB", "256GB")