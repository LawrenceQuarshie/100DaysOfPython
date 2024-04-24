fruits = ["apple", "banana", "cherry"]

a = ""
for i in range(len(fruits)):
    a += "<li>" + fruits[i] + "</li>\n"

b = "<ul>\n" + a + "</ul>"
print(b)
