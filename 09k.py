def prod_and_storage(name, *storages):
    for storage in storages:
        print(name, storage)

prod_and_storage("Samsung Galaxy A56", "128GB", "256GB")
prod_and_storage("Samsung Galaxy S25 Ultra", "256GB", "512GB", "1TB")
prod_and_storage("Samsung Galaxy S25 Plus", "256GB", "512GB")