txt = ("size", "faster", "less power") # as transistors shrink, they become faster, consume less power, and are cheaper to manufacture
y = list(txt)
y.append("cheaper")

txt = tuple(y)

print(txt)