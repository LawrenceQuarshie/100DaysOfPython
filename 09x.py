def product(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

product("Technical specifications", "Tecno", "Pop 9", month=11, year=2024)