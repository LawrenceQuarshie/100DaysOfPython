storage = 256
price = 17500

match price:
    case 17500 | 17000 | 25499 | 26220 if storage == 256:
        print("The phone is the 256GB storage option")
    case 17500 | 17000 | 25499 | 26220 if storage == 512:
        print("The phone is the 512GB storage option")