# Дан список [student1, student2, student3] с помощью цикла for добавить к каждому элементу списка слово “_good”.
# Вывести на экран.
a = ["student1", "student2", "student3"]
b = "_good"
for index, item in enumerate(a):
	item = item + "_good"
	a[index] = item

print('Обновленный список: ', a)

