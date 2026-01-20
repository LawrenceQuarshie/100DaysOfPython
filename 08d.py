def myfunction(brand, model):
    print("Full name:", brand, model)

product = {"brand": "Apple", "model": "iPhone 7"}
myfunction(**product)