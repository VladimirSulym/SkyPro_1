# Написать функцию, которая получает на вход список чисел и возвращает новый список, содержащий только числа,
# которые меньше среднего значения списка.
# Пример ввода:
# [1, 2, 3, 4, 5]
# Пример вывода:
# [1, 2]

def average_value(value):
    average = sum(value) / len(value)
    # result = []
    # for i in value:
    #     if i < average:
    #         result.append(i)
    # return result
    return [i for i in value if i < average]  # короткая запись предыдущих 5ти строк


print(average_value([1, 2, 3, 4, 5]))


# Написать функцию, которая получает на вход список строк и возвращает новый список, содержащий только уникальные
# строки.
# Пример ввода: ['apple', 'banana', 'orange', 'apple']
# Пример вывода: ['apple', 'banana', 'orange']

def unique_value(my_list):
    return sorted(set(my_list))


print(unique_value(['apple', 'banana', 'orange', 'apple']))


# Написать функцию, которая получает на вход список кортежей, содержащих информацию о товарах (например, название,
# цена, количество и т. д.), и возвращает новый список, отсортированный по убыванию цены.
# Пример ввода: [(apple, 2.5), (banana, 3.5), (orange, 1.5)]
# Пример вывода: [(banana, 3.5), (apple, 2.5), (orange, 1.5)]

def sorting_goods(my_list):
    # return sorted(my_list, key=lambda x: x[1], reverse=True) # альтернативное решение
    my_list.sort(key=lambda x: x[1], reverse=True)
    return my_list


print('TOTAL ->', sorting_goods([('apple', 2.5), ('banana', 3.5), ('orange', 1.5)]))


# Написать функцию, которая получает на вход список словарей, содержащих информацию о фильмах (например, название,
# жанр, режиссер и т. д.), и возвращает новый список, содержащий только те фильмы, которые относятся к заданному жанру.
# Пример ввода:
# [{title: 'The Shawshank Redemption', genre: 'Drama', director: 'Frank Darabont'},
# {title: 'The Godfather', genre: 'Crime', director: 'Francis Ford Coppola'},
# {title: 'The Dark Knight', genre: 'Action', director: 'Christopher Nolan'}], 'Drama'
#
# Пример вывода:
# [{title: 'The Shawshank Redemption', genre: 'Drama', director: 'Frank Darabont'}]


def filter_cinema(my_list, genre):
    return [i for i in my_list if i['genre'] == genre]
    # new_list = []
    # for i in my_list:
    #     if i['genre'] == genre:
    #         new_list.append(i)
    # return new_list

print(filter_cinema([{'title': 'The Shawshank Redemption', 'genre': 'Drama', 'director': 'Frank Darabont'},
                     {'title': 'The Godfather', 'genre': 'Crime', 'director': 'Francis Ford Coppola'},
                     {'title': 'The Dark Knight', 'genre': 'Action', 'director': 'Christopher Nolan'}], 'Drama'))

