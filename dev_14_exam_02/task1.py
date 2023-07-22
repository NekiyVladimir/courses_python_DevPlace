# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt. После этого удалите созданную папку.
#  Все операции выполнять с помощью встроенных функций библиотеки os.

import os
os.mkdir('C:/Users/Vladimir/Desktop/123') # создает папку
one = open('C:/Users/Vladimir/Desktop/123/test_1.txt', 'w') # создает файл
two = open('C:/Users/Vladimir/Desktop/123/test_2.txt', 'w')
three = open('C:/Users/Vladimir/Desktop/123/test_3.txt', 'w')
one.close()
two.close()
three.close()

os.rename('C:/Users/Vladimir/Desktop/123/test_1.txt', 'C:/Users/Vladimir/Desktop/123/rename_1.txt') # переименовываем
os.rename('C:/Users/Vladimir/Desktop/123/test_2.txt', 'C:/Users/Vladimir/Desktop/123/rename_2.txt')
os.rename('C:/Users/Vladimir/Desktop/123/test_3.txt', 'C:/Users/Vladimir/Desktop/123/rename_3.txt')

os.remove('C:/Users/Vladimir/Desktop/123/rename_1.txt') # удаление файла
os.remove('C:/Users/Vladimir/Desktop/123/rename_2.txt')
os.remove('C:/Users/Vladimir/Desktop/123/rename_3.txt')
os.rmdir('C:/Users/Vladimir/Desktop/123') # удаление папки
