resistors = ("fixed", "variable", "tapped")
resistor_list = list(resistors)
resistor_list.remove("fixed")

resistors = tuple(resistor_list)

print(resistors)