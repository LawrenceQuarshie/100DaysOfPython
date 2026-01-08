def myfunction(*args):
    a = 0
    for i in args:
        a += i
    
    return a

b = [1, 2, 3, 4]
result = myfunction(*b)
print(result)