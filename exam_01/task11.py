# Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.

a = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
b = []
c = ' '
for i in a:
    if c in i:
        b.append(i)
print(b, '- список, содержащий элементы с пробелами!')