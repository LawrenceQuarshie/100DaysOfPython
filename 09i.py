def prodstorage(*kargs):
    if len(kargs) == 1:
        path = "prod/template-1-option.html"
        print(path)
    elif len(kargs) == 2:
        path = "prod/template-2-options.html"
        print(path)
    elif len(kargs) == 3:
        path = "prod/template-3-options.html"
        print(path)
    elif len(kargs) == 4:
        path = "prod/template-4-options.html"
        print(path)

prodstorage("128GB", "256GB", "512GB")
prodstorage("128GB", "256GB")
prodstorage("256GB", "512GB", "1TB")
prodstorage("256GB", "512GB")