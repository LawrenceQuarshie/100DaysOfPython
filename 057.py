prod = {
    "prod1": {
        "name": "Tecno",
        "description": "Camon 40",
        "leastprice": 3285.10
    },
    "prod2": {
        "name": "Samsung",
        "description": "Galaxy A26",
        "leastprice": 2299.00
    },
    "prod3": {
        "name": "Samsung",
        "description": "Galaxy A36",
        "leastprice": 4330.00
    }
}

for x, obj in prod.items():
    print(x)

    for y in obj:
        print(y + ":" , obj[y])