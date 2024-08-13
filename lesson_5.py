# Задача 1
# line = "13f et3 5kk54"
#
# print(f"Пробелов {line.count(' ')} это процент -> {round(line.count(' ')/len(line)*100)}")
#
# Задача 2
# text_to_count = ("Статья рассказывает о последних научных открытиях в области "
#                  "исследования космоса. Интересно, что исследователи утверждают, "
#                  "что космическое время может быть относительным.")
# # word = input()
# # cont_word = 0
# #
# # print(text_to_count.find(word))
#
# Задача 3
# word_list = ["Это", "пример", "использования", "метода", "join", "в", "Python."]
#
# print(' '.join(word_list))
#
# input_word = input()
#
# print(input_word.count('р'))
#
# sentence = "Это пример использования метода split в Python."
#
# # разделили строку по строке split
# print(sentence.split('split'))

# Задача 5
# movie_scene = "В этой сцене герой произносит знаменитую фразу: 'Я всегда с вами'."
#
# what_to_replace = input()
# what_to_replace_it_with = input()
#
# print(movie_scene.replace(what_to_replace, what_to_replace_it_with))

# line = "A13f et3 D 5Kk54 M"
#
# upper_count = 0
# for i in line:
#     if i.isupper():
#         upper_count += 1
#
# print(upper_count)

# line = "abcdefghijklmnopqrstuvwxyz"
#
# border_user = input()
#
# border_user = border_user.split('-')
# print(border_user)
# split_total = line[int(border_user[0]):int(border_user[1])+1]
# print(split_total)
#
# date_string = "2023-12-19"
#
# print(':'.join(date_string.split("-")))
#
# year, month, day = date_string.split("-")
# print(f'Год:{year} месяц:{month} день:{day}')

word = input()

for i in range(0,len(word),):
  print(word[i:])
