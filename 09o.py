def myfunction(*numbers):
    if len(numbers) == 0:
        return None
    min_num = numbers[0]
    
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

print(myfunction(3, 7, 2, 9, 1))
print(myfunction(3, 7, 2, -9, 1))