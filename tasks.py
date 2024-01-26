# Строки:
# Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке.
# Создайте функцию, которая проверяет, является ли строка палиндромом (читается одинаково справа
# налево и слева направо).

user_str = input("Enter any string ")
reversed_str = user_str[::-1]
print(reversed_str)


def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False


print(is_palindrome(user_str))
