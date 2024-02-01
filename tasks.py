# Строки: ----------------------------------------------
#
# Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке.
# Создайте функцию, которая проверяет, является ли строка палиндромом (читается одинаково справа
# налево и слева направо).
#
# user_str = input("Enter any string ")
# reversed_str = user_str[::-1]
# print(reversed_str)
#
#
# def is_palindrome(str):
#     if str == str[::-1]:
#         return True
#     else:
#         return False
#
#
# print(is_palindrome(user_str))


# Списки: ----------------------------------------------
#
# Создайте список чисел и напишите программу для вывода только четных чисел из списка.
# Напишите функцию, которая принимает два списка и возвращает новый список, содержащий
# элементы, которые есть в обоих списках.

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []
# for i in my_list:
#     if i % 2 == 0:
#         result.append(i)
#
# print(result)
#
# myList_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# myList_2 = [2, 3, 4, 7, 6, 4, 77, 67, 34, 245, 55, 4, 3, 55, 5]
#
#
# def sum_lists(list1, list2):
#     general_elements = []
#     for value in list1:
#         if value in list2:
#             general_elements.append(value)
#     return general_elements
#
#
# print(sum_lists(myList_1, myList_2))


# Словари: -------------------------------
#
# Создайте словарь, представляющий информацию о человеке (имя, возраст, город и т.д.).
# Напишите программу, которая выводит всю информацию о человеке.
# Напишите функцию, которая принимает словарь и выводит все ключи этого словаря
# в отсортированном порядке.

# user_dict = {
#     'first_name': 'Alex',
#     'last_name': 'Simpson',
#     'email': 'abc@rr.com',
#     'age': 23,
#     'gender': 'male',
#     'city': 'Kiev',
# }
#
# user_info = ''
# for _, value in user_dict.items():
#     if type(value) != str:
#         value = str(value)
#         user_info += ' ' + value
#     else:
#         user_info += ' ' + value
# print(user_info)
#
#
# def key_user(any_user_dict):
#     key_user_dict = sorted(any_user_dict.keys())
#     return key_user_dict
#
#
# print(key_user(user_dict))


# st = "spam"
# print(st[-1::-1])

# st ="spam"
# for x in st:
#     print(x, end="_")

