def myfunction(*numbers):
    total = 0
    for number in numbers:
        total += number
    
    return total

print(myfunction(1, 2, 3))
print(myfunction(10, 20, 30, 40))
print(myfunction(5))