# 1. Даны два словаря:dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python.

# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update((dictionary_2))
# print(dictionary_1)

# 2. Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами. Выведите полученный словарь на экран.

# a = [1,2,3]
# b = [0,0,0]
# d1 = dict(zip(a,b))
# d2 = {}
# print(f'Первый способ: {d1}')
# for i in range(1,4):
#     d2[i] = b[i-1]
# print(f'Второй способ: {d2}')
# d3 = dict.fromkeys(a, 0)
# print(f'Третий способ: {d3}')

# 3. Задан список слов, в которых встречается символ ‘_’ подчеркивание).
# Создать новый список, в котором символ подчеркивания в словах ‘_’ заменить символом ‘ ‘ (пробел).
# l = [ "ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__" ]
# a = []
# b = '_'
# c = ' '
# for i in l:
#     if b in i:
#         d = i.replace('_',' ')
#         a.append(d)
# print(a)

# 4. На вход программы подается словарь a = {1:10, 2:20, 3:30}, необходимо получить список произведения
# ключа на значение.

# a = {1:10, 2:20, 3:30}
# b = [k*v for k,v in a.items()]
# print(b)

# 5. Выведите статистику частности букв в кортеже
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и’)
# Примечание: Статистика частности - число повторений каждой из букв.

# long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
# print(long_word)
# a = {}
# for i in long_word:
#     if i in  a.keys():
#         continue
#     else:
#         a[i] = long_word.count(i)
# print(a)

# 6. Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()

# a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# b = list(a.keys())
# for i in b:
#     a[i+str(len(i))] = a.pop(i)
# print(a)


