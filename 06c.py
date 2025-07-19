installed = 11165.4 # MW installed capacity in Nigeria
dependable = 4000.0 # MW dependable capacity in Nigeria

print("Under utilization of Nigeria's grid") if installed > dependable else print("Over utilization of Nigeria's grid")