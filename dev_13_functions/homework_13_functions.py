# 1. Простейший калькулятор c введёнными двумя числами вещественного типа. Ввод с клавиатуры: операции + - * / и
# два числа. Операции являются функциями. Обработать ошибку: “Деление на ноль” Ноль использовать в качестве завершения
# программы (сделать как отдельную операцию).

# while True:
#
#     def oper1(a,b):
#         return a + b
#
#     def oper2(a,b):
#         return a - b
#
#     def oper3(a,b):
#         return a * b
#
#     def oper4(a,b):
#         return a / b
#
#     c = input('Введите операцию, которую вы хотите выполнить: ')
#     a = float(input('Введите первое число: '))
#     if a == 0:
#         print('Работа окончена!')
#         break
#     b = float(input('Введите второе число: '))
#

#     if b == 0:
#         print('Делить на 0 нельзя!')
#         b = float(input('Введите второе число: '))
#     elif c not in ('+','-', '*', '/'):
#         print('Неправильно введен знак операции!')
#         c = input('Введите операцию, которую вы хотите выполнить: ')
#     if c == '+':
#         print(oper1(a,b))
#     elif c == '-':
#         print(oper2(a,b))
#     elif c == '*':
#         print(oper3(a,b))
#     elif c == '/':
#         print(oper4(a,b))

# 2. Если в функцию передается кортеж, то посчитать длину всех его слов. Если список, то посчитать кол-во букв и
# чисел в нем. Число - количество нечетных цифр. Строка - количество букв.

# def func(a):
#     summa = 0
#     numbers = 0
#     if type(a) == type(tuple()):
#         for i in a:
#             summa += len(str(i))
#         return 'Длина всех слов коретжа равна: ' + str(summa)
#     elif type(a) == type([]):
#         for i in a:
#             if type(i) == type(str()):
#                 summa += len(i)
#             elif type(i) == type(int()):
#                 numbers += 1
#         return 'Количество всех букв равно: ' + str(summa) + ' Количество всех чисел равно: ' + str(numbers)
#         'Количество всех чисел равно: ' + str(numbers)
#     elif type(a) == type(int()):
#         for i in range(0,len(str(a))):
#             a = str(a)
#             if int(a[i]) % 2 == 1:
#                 summa += 1
#         return 'Количество нечетных цифр равно: ' + str(summa)
#     elif type(a) == type(str()):
#         return 'Количество букв: ' + str(len(a))

# 3. Функция для вывода таблицы умножения для указанного числа.

# a = int(input('Введите число: '))
# def table_numbers(a):
#     for i in range(1,11):
#         print(f'{i} x {a} = {i*a}')
#
# table_numbers(a)

# 4. Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(), которая в качестве
# аргумента принимает другую функцию (главное, не встроенную, built-in). В результате работы она выводит следующие
# данные: название анализируемой функции, наименование всех принимаемых ею параметров и их типы (позиционные, ключевые
# и т.п.). Попробуйте повторить результат девушки.
# import inspect
# def inspect_function(func):
#     print('Имя функции: ',func.__name__)
#     a = str(inspect.signature(func))
#     b = len(a)
#     lst = a[1:b].split(',')
#     for i in lst:
#         if '=' in i.strip():
#             i = i.replace(")", "")
#             print(f'Ключевой аргумент функции {func.__name__}: ', i)
#         else:
#             print(f'Позиционный аргумент функции {func.__name__}: ', i)
#
# def one(a,b,c=2):
#     pass
#
# inspect_function(one)