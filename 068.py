thermal = 68 # 68% of Ghana's electricity from thermal/natural gas
hydro = 29 # 29% of Ghana's electricity from hydro
renewables = 3 # 3% of Ghana's electricity from thermal/natural gas

if thermal > hydro:
    print("The main power source in Ghana is thermal")
elif thermal == hydro:
    print("The main power sources are both thermal and hydro")
else:
    print("The main power source in Ghana is hydro")