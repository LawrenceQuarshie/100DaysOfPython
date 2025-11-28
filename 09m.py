def prodbrandtotal(prod, *totals):
    sumtotal = 0
    for total in totals:
        sumtotal += total
    
    return "There are " + str(sumtotal) + " " + prod + " product offerings on our website"

print(prodbrandtotal("Apple", 13, 9, 7))
print(prodbrandtotal("Samsung", 56, 35, 20))
print(prodbrandtotal("Huawei", 6, 3, 5))