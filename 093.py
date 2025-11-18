def temp2K(temp, unit):
    if unit == "C":
        return temp + 273.15
    else:
        return (temp - 32) * (5/9) + 273.15
    
result = temp2K(10, "C")
result2 = temp2K(1, "F")
print(result)
print(result2)