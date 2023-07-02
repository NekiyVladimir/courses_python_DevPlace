# Написать программу для вычисления значения выражений.
# Проверить правильность выполнения задания с помощью тестовых значений.

import math
a = float(input("Введите число альфа: "))
b = float(input("Введите число бета: "))
g = float(input("Введите число гамма: "))
y = (1/4)*(math.sin(a+b-g)+math.sin(b+g-a)+math.sin(g+a-b)-math.sin(a+b+g))
print('Ответ: ', y)

# test

a = 1
b = 3
g = 0.25

y = (1/4)*(math.sin(a+b-g)+math.sin(b+g-a)+math.sin(g+a-b)-math.sin(a+b+g))
print('Ответ: ', y)