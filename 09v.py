def myproduct(fullname, **specs):
    print("Full Name:", fullname)
    for key, value in specs.items():
        print(key + ":", value)

myproduct(fullname="Apple iPhone 8", weight=148.0, colour="Silver, Space Gray, Gold, Red", cpu="Hexa Core")
print("")
myproduct(fullname="Teledyne LeCroy HDO6034B", samplerate="10 GS/s on 4 Ch with ESR", maxacqmem="250 Mpts", inputs=4, vres="12-bit")