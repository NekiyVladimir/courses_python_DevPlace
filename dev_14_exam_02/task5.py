# Есть словарь песен группы Depeche Mode violator songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43,
# 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
#  Выведите общее время звучания всех песен. Создайте список песен, время звучаниях которых больше 5 минут
#  Создайте новый словарь тех песен, в название которых состоит из одного слова.

a = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
      'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18,
      'Clean': 5.68}
summa = 0
lst_songs = []
lst_one = []
for k,v in a.items():
      summa += v
      if v < 5:
            lst_songs.append(k)
      if " " not in k:
            lst_one.append(k)
print(f'Общее время звучания всех песен: {summa} мин')
print(f'Список песен, время звучания которых не превышает 5 мин - {lst_songs}')
print(f'Список песен, название которых состоит из одного слова: {lst_one}')