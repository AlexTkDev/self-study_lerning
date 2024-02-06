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


def most_frequent(data: list[str]) -> str:
    most_common = None
    counter = 0

    for item in data:
        a = data.count(item)
        if a > counter:
            most_common = item
            counter += 1

    return most_common


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(['a', 'b', 'c', 'a', 'b', 'a']) == 'a'
assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
assert most_frequent(['a']) == 'a'
assert most_frequent(['a', 'a']) == 'a'
assert most_frequent(['a', 'a', 'z']) == 'a'

print("The mission is done! Click 'Check Solution' to earn rewards!")
