price = 10500
match price:
    case 8500 | 8990 | 5100 | 9500:
        print("Price is in the 1,000 range")
    case 10400 | 10500:
        print("Price in the 10,000 range")