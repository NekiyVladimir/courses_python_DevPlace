# Необходимо удалить пустые строки из списка строк.
a = ["", "a", "", "ada", "", "aba"]
for i in a:
    if i == "":
        a.remove(i)
print(a)