def myfunction(a, b, /, *, c, d):
    return a + b + c + d

result = myfunction(5, 10, c = 15, d = 20)
print(result)