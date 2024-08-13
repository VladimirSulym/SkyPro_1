# list_animals = ['deer', 'bear', 'rabbit', 'butterfly']
# list_number = [123, 214, 2465, 5743]
#
# print(list_animals)
# print(type(list_number))
# print(list_number[1])
# print(type(list_number[1]))
#
# print(len(list_animals))
#
# list_animals.extend([123,43,23423])
# print(list_animals)
#
list1 = [4, 1, 8, 7, 2, 1, 11, 23, 2, 2]
# user_input = int(input())
#
# if user_input in list1:
#     print('Число есть')
# else:
#     print('Числа НЕТ')

# user_input_num1 = int(input())
# user_input_num2 = int(input())
#
# if user_input_num1 in list1 and user_input_num2 in list1:
#     print('Оба числа в списке')
# elif user_input_num1 in list1 or user_input_num2 in list1:
#     print('Одно из чисел в списке')
# else:
#     print('Чисел в списке НЕТ')
#
# quant_num1 = list1.count(1)
# quant_num2 = list1.count(2)
#
# print(f'Первое число повторяется {quant_num1} раз, а второй {quant_num2} раз их сумма равна {quant_num1 + quant_num2}')

list2 = [6, 3, 6, 12, 22, 41, 1, 3, 32, 42]

# avg_num1 = sum(list1) / len(list1)
# avg_num2 = sum(list2) / len(list2)
#
# print(avg_num1, avg_num2)
#
# if avg_num1 > avg_num2:
#     print('1 больше')
# elif avg_num2 > avg_num1:
#     print('2 больше')
# else:
#     print('Равны')

# print(sorted(list1)[-1])
# print(sorted(list2)[-1])
# print(max(list1))
#
# numbers_1 = [1, 2, 3, 4, 5, 6, 7]
# numbers_2 = [8, 9, 10, 11, 12]
#
# numbers_1.extend(numbers_2)
# print(numbers_1)

# Задача 7
# Есть список чисел.
# numbers = [4, 5, 7, 8, 10, 42, 2, 5, 15, 27, 33, 46, 99, 124]
# Запросите у пользователя индекс элемента для удаления, удалите
# элемент по этому индексу из списка и выведите результат.

# numbers = [4, 5, 7, 8, 10, 42, 2, 5, 15, 27, 33, 46, 99, 124]
# user_num = int(input())
#
# if user_num < len(numbers)-1:
#     print(numbers.pop(user_num))
# else:
#     print('Такого индекса нет')


# Есть список чисел.
# numbers = [4, 5, 7, 8, 10, 42, 2, 5, 15, 27, 33, 46, 99, 124]
# Запросите у пользователя начальный и конечный индексы. Выведите подсписок,
# содержащий элементы с индексами от начального до конечного (включительно).

# numbers = [4, 5, 7, 8, 10, 42, 2, 5, 15, 27, 33, 46, 99, 124]
# user_num_start = int(input())
# user_num_finish = int(input())
#
# if user_num_start < len(numbers)-1 and user_num_finish < len(numbers)-1:
#     if user_num_start > user_num_finish:
#         # temp_num = user_num_start
#         # user_num_start = user_num_finish
#         # user_num_finish = temp_num
#         user_num_start, user_num_finish = user_num_finish, user_num_start # альтернативный вариант кода
#     print(numbers[user_num_start:user_num_finish+1])
# else:
#     print("Значение не входит в диапазон")

# Есть список чисел.
# numbers = [4, 5, 7, 8, 10, 42, 2, 5, 15, 27, 33, 46, 99, 124]
# Вставьте новое число 15 в середину списка.

# numbers = [4, 5, 7, 8, 10, 42, 2, 5, 15, 27, 33, 46, 99, 124]
# user_num = int(input())
# numbers.insert(int(len(numbers)/2), user_num)
# print(numbers)

print(list1)
print(list1[-3:])

list1[1:3] = [222, 222]
print(list1)

numbers = [4, 2, 9, 1, 5]
numbers.sort()
print(numbers)