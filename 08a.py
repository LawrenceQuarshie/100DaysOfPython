def myfunction(*storage):
    labels = []
    for i in range(len(storage)):
        labels.append("obj" + str(i))
    
    return labels

storage = ["64GB", "128GB", "256GB"]
result = myfunction(*storage)
print(result)