def myplcspecs(**plcdata):
    print(type(plcdata))
    print("Manfacturer:", plcdata["brand"])
    print("Year of release:", plcdata["year"])
    print("All data:", plcdata)

myplcspecs(brand = "Siemens", year = 2012, model = "Simatic S7-1500")