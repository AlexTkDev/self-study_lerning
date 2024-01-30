# arithmetic mean
# result = 0
# count = 0
# temp_var = 0
#
# def mean(*digit):
#     global temp_var, count, result
#     for num in digit:
#         temp_var += num
#         count += 1
#     result += temp_var / count
#     return result
#
#
# print(round(mean(2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 7, 8, 7, 7, 7, 8, 8, 9, 8, 8), 2))

# перевод из десятичной в двоичную систему

# def convert_num(number):
#     if number > 0:
#         return number % 2 + 10 * convert_num(number // 2)
#     else:
#         return 0
#
#
# num = int(input("Enter a number: "))
# print(convert_num(num))

# random generate

import random
import string

alphanum = "0123456789!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
length = 12

password = ''.join(random.choice(alphanum) for _ in range(length))

print(password)
