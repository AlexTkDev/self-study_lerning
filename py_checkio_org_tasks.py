"""
    Дано текст і потрібно знайти його перше слово.
    Даний текст містить англійські букви та пробіли.
    На початку та у кінці пробілів немає.
"""

# def first_word(text: str) -> str:
#     # your code here
#     return text.split(" ")[0]
#
#
# print("Example:")
# print(first_word("Hello world"))
#
# # These "asserts" are used for self-checking
# assert first_word("Hello world") == "Hello"
# assert first_word("a word") == "a"
# assert first_word("greeting from CheckiO Planet") == "greeting"
# assert first_word("hi") == "hi"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
    Перевір, чи є вхідне число парним чи ні. Твоя функція повинна повертати True, якщо число парне, 
    і False, якщо число непарне.
    Вхідні дані: Ціле число.
    Вихідні дані: Булеве (логічне) значення.
    
### Эта функция is_even проверяет, является ли число четным. 
    Она использует битовую операцию AND с числом 1 (num & 1).
     Если число четное, то младший бит (последний бит) равен 0, и результат выражения num & 1 будет равен 0. 
     Затем оператор not инвертирует результат, так что если num & 1 равно 0 (число четное), 
     то not(num & 1) будет True, что и означает, что число четное.

"""

# def is_even(num: int) -> bool:
#     # your code here
#     return num & 1 == 0
#
#
# print("Example:")
# print(is_even(2))
#
# # These "asserts" are used for self-checking
# assert is_even(2) == True
# assert is_even(5) == False
# assert is_even(0) == True
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
    У тебе є послідовність рядків і тобі потрібно визначити,
     який рядок зустрічається найчастіше у цій сукупності.
"""


# def most_frequent(data: list[str]) -> str:
#     # most_common = None
#     # counter = 0
#     #
#     # for item in data:
#     #     a = data.count(item)
#     #     if a > counter:
#     #         most_common = item
#     #         counter += 1
#     #
#     # return most_common
#
#     # or
#     return max(data, key=data.count)
#
#
# print("Example:")
# print(most_frequent(["a", "b", "c", "a", "b", "a"]))
#
# # These "asserts" are used for self-checking
# assert most_frequent(['a', 'b', 'c', 'a', 'b', 'a']) == 'a'
# assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
# assert most_frequent(['a']) == 'a'
# assert most_frequent(['a', 'a']) == 'a'
# assert most_frequent(['a', 'a', 'z']) == 'a'
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
    У заданому тексті тобі потрібно підсумувати числа, виключивши будь-які цифри,
     які є частиною слова.
    Текст складається з чисел, пробілів та літер з англійського алфавіту.
"""


# def sum_numbers(text: str) -> int:
#     res = 0
#     is_digit = text.split()
#     if len(is_digit) == 0:
#         res = 0
#     else:
#         for num in is_digit:
#             if num.isdigit():
#                 res += int(num)
#     return res
#
# # or
# # sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())
#
# ## or
# ## def sum_numbers(text: str) -> int:
#     return sum(map(int, filter(str.isdigit, text.split())))
#
# print("Example:")
# print(sum_numbers("hi"))
#
# # These "asserts" are used for self-checking
# assert sum_numbers("hi") == 0
# assert sum_numbers("who is 1st here") == 0
# assert sum_numbers("my numbers is 2") == 2
# assert (
#     sum_numbers(
#         "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#     )
#     == 3755
# )
# assert sum_numbers("5 plus 6 is") == 11
# assert sum_numbers("") == 0
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
    Твоя задача знайти, на яку кількість нулів закінчується передане число.
"""

#
# def end_zeros(a: int) -> int:
#     # your code here
#     return len(str(a)) - len(str(a).strip("0"))
#
#
# print("Example:")
# print(end_zeros(10))
#
# # These "asserts" are used for self-checking
# assert end_zeros(0) == 1
# assert end_zeros(1) == 0
# assert end_zeros(10) == 1
# assert end_zeros(101) == 0
# assert end_zeros(245) == 0
# assert end_zeros(100100) == 2
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
    У цій місії ви повинні перевірити, чи всі елементи вказані в списку є однаковими.
"""

# from typing import List, Any
#
#
# def all_the_same(elements: List[Any]) -> bool:
#     res = all(x == elements[0] for x in elements)
#     return res
#
#
# print("Example:")
# print(all_the_same([1, 1, 1]))
#
# # These "asserts" are used for self-checking
# assert all_the_same([1, 1, 1]) == True
# assert all_the_same([1, 2, 1]) == False
# assert all_the_same([1, "a", 1]) == False
# assert all_the_same([1, 1, 1, 2]) == False
# assert all_the_same([]) == True
# assert all_the_same([1]) == True
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
    Твоє завдання тут, це створити функцію, що приймає кортеж і повертає кортеж лише з 3 елементами - першим,
    третім елементами від початку і другим елементом від кінця вхідного кортежу.
 """

#
# def easy_unpack(elements: tuple) -> tuple:
#     new_list = [elements[0], elements[2], elements[-2]]
#     return tuple(new_list)
#
#
# print("Example:")
# print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
#
# # These "asserts" are used for self-checking
# assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
# assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
# assert easy_unpack((6, 3, 7)) == (6, 7, 3)
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
    Вам нужно подсчитать количество цифр в данной строке.
"""


def count_digits(text: str) -> int:
    res = list(filter(str.isdigit, text))
    return len(res)


print("Example:")
print(count_digits(""))

# These "asserts" are used for self-checking
assert count_digits("hi") == 0
assert count_digits("who is 1st here") == 1
assert count_digits("my numbers is 2") == 1
assert (
        count_digits(
            "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
        )
        == 8
)
assert count_digits("5 plus 6 is") == 2
assert count_digits("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")


