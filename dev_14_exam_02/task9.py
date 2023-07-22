# Сын Уилла Смита, Джейден Смит, является кинозвездой, такой как «Ребенок-карате» (2010) и «После Земли» (2013). Джейден также известен некоторыми философскими идеями, которые он предлагает через Twitter. При написании статей в Twitter он почти всегда использует заглавные буквы для каждого слова.
#
# Задача - преобразовать строку в письмо Джейдена Смита. Эти строки принадлежат Джейдену Смиту, но они не пишутся с заглавной буквы так, как он их изначально набирал.
#
# пример:
#
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

string = "How can mirrors be real if our eyes aren't real"
string = string.split()
for i in range(0, len(string)):
    string[i] = string[i].capitalize()
print(" ".join(string))