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
import random
import re
import statistics
import string
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


# def count_digits(text: str) -> int:
#     res = list(filter(str.isdigit, text))
#     return len(res)
#
#
# print("Example:")
# print(count_digits(""))
#
# # These "asserts" are used for self-checking
# assert count_digits("hi") == 0
# assert count_digits("who is 1st here") == 1
# assert count_digits("my numbers is 2") == 1
# assert (
#         count_digits(
#             "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#         )
#         == 8
# )
# assert count_digits("5 plus 6 is") == 2
# assert count_digits("") == 0
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from collections.abc import Iterable
#
#
# def remove_all_before(items: list, border: int) -> Iterable:
# #     try:
# #         return items[items.index(border):]
# #     except ValueError:
# #         return items
#
#     ## or
#     return items[items.index(border):] if border in items else items
#
#
# print("Example:")
# print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
#
# # These "asserts" are used for self-checking
# assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
# assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
# assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
# assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
# assert list(remove_all_before([], 0)) == []
# assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [
#     7,
#     7,
#     7,
#     7,
#     7,
#     7,
#     7,
#     7,
#     7,
# ]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from collections.abc import Iterable
#
#
# def replace_first(items: list) -> Iterable:
#     if len(items) <= 1:
#         return items
#
#     last_item = items.pop(0)
#     items.insert(len(items), last_item)
#     return items
#
# # These "asserts" are used for self-checking
# print("Example:")
# print(list(replace_first([1, 2, 3, 4])))
#
# assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# assert replace_first([1]) == [1]
# assert replace_first([]) == []
# assert replace_first([1, 2, 2, 2]) == [2, 2, 2, 1]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def max_digit(value: int) -> int:
#     return max(int(k) for k in str(value))
#
#
# print("Example:")
# print(max_digit(10))
#
# # These "asserts" are used for self-checking
# assert max_digit(0) == 0
# assert max_digit(52) == 5
# assert max_digit(634) == 6
# assert max_digit(1) == 1
# assert max_digit(10000) == 1
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def beginning_zeros(a: str) -> int:
#     count = 0
#     for letter in a:
#         if letter in "0":
#             count += 1
#         else:
#             break
#     return count
#
#
# print("Example:")
# print(beginning_zeros("10"))
#
# # These "asserts" are used for self-checking
# assert beginning_zeros("100") == 0
# assert beginning_zeros("001") == 2
# assert beginning_zeros("100100") == 0
# assert beginning_zeros("001001") == 2
# assert beginning_zeros("012345679") == 1
# assert beginning_zeros("0000") == 4
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def between_markers(text: str, start: str, end: str) -> str:
#     s = text.find(start)
#     e = text.find(end)
#     return text[s + 1:e]
#
#
# print("Example:")
# print(between_markers("What is >apple<", ">", "<"))
#
# # These "asserts" are used for self-checking
# assert between_markers("What is >apple<", ">", "<") == "apple"
# assert between_markers("What is [apple]", "[", "]") == "apple"
# assert between_markers("What is ><", ">", "<") == ""
# assert between_markers("[an apple]", "[", "]") == "an apple"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from typing import Iterable
# from textwrap import wrap
#
#
# def split_pairs(text: str) -> Iterable[str]:
#     return list(map(''.join, zip(*[iter(text + '_')]*2)))
#
#     # or
#     # return (wrap(text if len(text) % 2 == 0 else text + '_', 2))
#
#
#
# print("Example:")
# print(list(split_pairs("abcd")))
#
# assert list(split_pairs("abcd")) == ["ab", "cd"]
# assert list(split_pairs("abc")) == ["ab", "c_"]
# assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
# assert list(split_pairs("a")) == ["a_"]
# assert list(split_pairs("")) == []
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def nearest_value(values: set[int], one: int) -> int:
#     new_values = list(values)
#     new_values.sort()
#     dif = [abs(i - one) for i in new_values]
#     return new_values[dif.index(min(dif))]
#
#
# print("Example:")
# print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
#
# assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
# assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
# assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
# assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
# assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
# assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
# assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
# assert nearest_value({2, 3, -1}, 0) == -1
# assert nearest_value({5}, 5) == 5
# assert nearest_value({5}, 7) == 5
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from collections.abc import Iterable
#
#
# def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
#     # result = []
#     # for key in donuts:
#     #     if key == 0:
#     #         a_temp = [int(i) for i in str(key) * 2]
#     #         result.append(a_temp[0])
#     #         result.append(a_temp[1])
#     #     else:
#     #         result.append(key)
#     #
#     # return result
#
#     #or
#     # return sum([[i] if i else [0, 0] for i in donuts], [])
#
#     # or
#     for donut in donuts:
#         if donut == 0:
#             yield 0
#         yield donut
#     return []
#
#
# print("Example:")
# print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))
# #
# # # These "asserts" are used for self-checking
# assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
#     1,
#     0,
#     0,
#     2,
#     3,
#     0,
#     0,
#     4,
#     5,
#     0,
#     0,
# ]
# assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
# assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from collections.abc import Iterable
#
#
# def checkio(data: list[int]) -> Iterable[int]:
#     # result = []
#     # for i in data:
#     #     if data.count(i) != 1:
#     #         result.append(i)
#     # return result
#
#     # or
#     return (i for i in data if data.count(i) != 1)
#
#
# print("Example:")
# print(list(checkio([1, 2, 3, 1, 3])))
#
# # These "asserts" are used for self-checking
# assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
# assert list(checkio([1, 2, 3, 4, 5])) == []
# assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
# assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
# assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
# assert list(checkio([10, 20, 30, 10])) == [10, 10]
# assert list(checkio([7])) == []
# assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
# assert list(checkio([99, 98, 99])) == [99, 99]
# assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
# assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def checkio(array: list[int]) -> int:
#     # if len(array) == 0:
#     #     res = 0
#     # else:
#     #     res = sum(i for i in array[::2]) * array[-1]
#     # return res
#
#     # or
#     # if len(array) == 0: return 0
#     # return sum(array[0::2] * array[-1])
#
#     # or
#     return sum(array[0::2])*array[-1] if 0 < len(array) else 0
#
#
# print("Example:")
# print(checkio([0, 1, 2, 3, 4, 5]))
#
# # These "asserts" are used for self-checking
# assert checkio([0, 1, 2, 3, 4, 5]) == 30
# assert checkio([1, 3, 5]) == 30
# assert checkio([6]) == 36
# assert checkio([]) == 0
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def left_join(phrases: tuple[str]) -> str:
#     # return ','.join(phrase.replace("right", "left") for phrase in phrases)
#
#     result = []
#     for phrase in phrases:
#         phrase = phrase.replace("right", "left")
#         result.append(phrase)
#     return ','.join(result)
#
#
# print("Example:")
# print(left_join(("left", "right", "left", "stop")))
#
# # These "asserts" are used for self-checking
# assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
# assert left_join(("brightness wright",)) == "bleftness wleft"
# assert left_join(("enough", "jokes")) == "enough,jokes"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# between_markers = lambda text, start, end: text[text.find(start) + 1: text.find(end)] if (idx_start := text.find(
#     start)) != -1 and idx_start < text.find(end) else ''
#
# print("Example:")
# print(between_markers("What is >apple<", ">", "<"))
#
# # These "asserts" are used for self-checking
# assert between_markers("What is >apple<", ">", "<") == "apple"
# assert between_markers("What is [apple]", "[", "]") == "apple"
# assert between_markers("What is ><", ">", "<") == ""
# assert between_markers("[an apple]", "[", "]") == "an apple"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def between_markers(text: str, begin: str, end: str) -> int:
#     idx_begin = text.find(begin)
#     idx_end = text.find(end)
#     if idx_begin == -1 or idx_end == -1 or idx_begin > idx_end:
#         return ""
#     return text[idx_begin + len(begin):idx_end]
#
# print("Example:")
# print(between_markers("What is >apple<", ">", "<"))
#
# # These "asserts" are used for self-checking
# assert between_markers("What is >apple<", ">", "<") == "apple"
# assert between_markers("What is [apple]", "[", "]") == "apple"
# assert between_markers("What is ><", ">", "<") == ""
# assert between_markers("[an apple]", "[", "]") == "an apple"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def first_word(text: str) -> str:
#     text = text.replace('.', ' ').replace(',', ' ')
#     text = text.strip().split()
#     return text[0]
#
#
# print("Example:")replace

# print(first_word('Hello World'))
#
# # These "asserts" are used for self-checking
# assert first_word("Hello world") == "Hello"
# assert first_word(" a word ") == "a"
# assert first_word("don't touch it") == "don't"
# assert first_word("greetings, friends") == "greetings"
# assert first_word("... and so on ...") == "and"
# assert first_word("hi") == "hi"
# assert first_word('Hello.World') == 'Hello'
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def checkio(words: str) -> bool:
#     new_words = words.split()
#     for triple in zip(new_words, new_words[1:], new_words[2:]):
#         if all(word.isalpha() for word in triple):
#             return True
#     return False
#
#
# print("Example:")
# print(checkio("Hello World hello"))
#
# # These "asserts" are used for self-checking
# assert checkio("Hello World hello") == True
# assert checkio("He is 123 man") == False
# assert checkio("1 2 3 4") == False
# assert checkio("bla bla bla bla") == True
# assert checkio("Hi") == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# from dateutil.parser import parse
#
#
# def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
#     a_tmp = [str(i) for i in a]
#     b_tmp = [str(i) for i in b]
#     a_tmp = '/'.join(a_tmp)
#     b_tmp = '/'.join(b_tmp)
#     date1 = parse(a_tmp)
#     date2 = parse(b_tmp)
#     num_days = abs((date2 - date1).days)
#     return num_days
#
# print("Example:")
# print(days_diff((1982, 4, 19), (1982, 4, 22)))
#
# assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
# assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
# assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# # from datetime import datetime
# #
# # def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
# #     a_tmp = '{:04d}/{:02d}/{:02d}'.format(*a)
# #     b_tmp = '{:04d}/{:02d}/{:02d}'.format(*b)
# #
# #     date1 = datetime.strptime(a_tmp, '%Y/%m/%d')
# #     date2 = datetime.strptime(b_tmp, '%Y/%m/%d')
# #     num_days = abs((date2 - date1).days)
# #     return num_days
#
# # or
# from datetime import date
# days_diff = lambda f, t: abs((date(*f) - date(*t)).days)
# #
# # print("Example:")
# # print(days_diff((696, 5, 7), (9241, 6, 27)))
# #
# # assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
# # assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
# # assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
# # assert days_diff((1, 1, 1), (9999, 12, 31)) == 3652058
# # assert days_diff((696, 5, 7), (9241, 6, 27)) == 3121048
# #
# # print("The mission is done! Click 'Check Solution' to earn rewards!")


# def backward_string_by_word(text: str) -> str:
#     a = text.split(" ")
#     res = " ".join(a[::-1])
#     return res[::-1]
#
#
# print("Example:")
# print(backward_string_by_word("hello world"))
#
# # These "asserts" are used for self-checking
# assert backward_string_by_word("") == ""
# assert backward_string_by_word("world") == "dlrow"
# assert backward_string_by_word("hello world") == "olleh dlrow"
# assert backward_string_by_word("hello   world") == "olleh   dlrow"
# assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def changing_direction(elements: list[int]) -> int:
#     if len(elements) <= 1:
#         return 0
#
#     last_direction = None
#     direction_changes = 0
#
#     for i in range(1, len(elements)):
#         current_element = elements[i]
#         previous_element = elements[i - 1]
#
#         if current_element > previous_element:
#             current_direction = "up"
#         elif current_element < previous_element:
#             current_direction = "down"
#         else:
#             current_direction = last_direction
#
#         if last_direction != current_direction:
#             direction_changes += 1
#
#         last_direction = current_direction
#
#     res = direction_changes -1
#
#     return res
#
#
# print("Example:")
# print(changing_direction([1, 2, 3, 4, 5]))
#
# # These "asserts" are used for self-checking
# assert changing_direction([1, 2, 3, 4, 5]) == 0
# assert changing_direction([1, 2, 3, 2, 1]) == 1
# assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def bigger_price(limit: int, data: list[dict]) -> list[dict]:
#     sorted_data = sorted(data, key=lambda x: x['price'], reverse=True)
#     return sorted_data[:limit]
#
#
#
# print("Example:")
# print(
#     bigger_price(
#         2,
#         [
#             {"name": "bread", "price": 100},
#             {"name": "wine", "price": 138},
#             {"name": "meat", "price": 15},
#             {"name": "water", "price": 1},
#         ],
#     )
# )
#
# assert bigger_price(
#     2,
#     [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1},
#     ],
# ) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
# assert bigger_price(
#     1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
# ) == [{"name": "whiteboard", "price": 170}]

# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def popular_words(text: str, words: list) -> dict:
#     text = text.lower().split()
#     word_count = {word: text.count(word) for word in words}
#     return word_count
#
#
# print("Example:")
# print(
#     popular_words(
#         """
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# """,
#         ["i", "was", "three", "near"],
#     )
# )
#
# assert popular_words(
#     "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
#     ["i", "was", "three", "near"],
# ) == {"i": 4, "was": 3, "three": 0, "near": 0}
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# def second_index(text: str, symbol: str) -> int | None:
#     a = []
#     for i in enumerate(text):
#         if symbol in i[1]:
#             a.append(i[0])
#
#     return a[1] if len(a) >= 2 else None
#
#
#
#
# print("Example:")
# print(second_index("sims", "s"))
#
# # These "asserts" are used for self-checking
# assert second_index("sims", "s") == 3
# assert second_index("find the river", "e") == 12
# assert second_index("hi", " ") == None
# assert second_index("hi mayor", " ") == None
# assert second_index("hi mr Mayor", " ") == 5
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def between_markers(text: str, begin: str, end: str) -> int:
#     # idx_begin = text.find(begin)
#     # idx_end = text.find(end)
#     # if idx_begin == -1 and idx_end > -1:
#     #     return text[:idx_end]
#     # elif idx_end == -1 and idx_begin > -1:
#     #     return text[idx_begin + len(begin):]
#     # elif idx_end == -1 and idx_begin == -1:
#     #     return text
#     # elif idx_begin == -1 or idx_end == -1 or idx_begin > idx_end:
#     #     return ""
#     # else:
#     #     return text[idx_begin + len(begin):idx_end]
#
#     # or
#     idx_begin = text.find(begin)
#     idx_end = text.find(end)
#
#     match (idx_begin == -1, idx_end == -1):
#         case (True, True):
#             return text
#         case (True, False):
#             return text[:idx_end]
#         case (False, True):
#             return text[idx_begin + len(begin):]
#         case _:
#             return text[idx_begin + len(begin):idx_end]
#
#
# print("Example:")
# print(between_markers("No hi", "[b]", "[/b]"))
#
# assert between_markers("What is >apple<", ">", "<") == "apple"
# assert (
#     between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
#     == "My new site"
# )
# assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
# assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
# assert between_markers("No hi", "[b]", "[/b]") == "No hi"
# assert between_markers("No <hi>", ">", "<") == ""
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def missing_number(items: list[int]) -> int:
#     sorted_items = sorted(items)
#     step = sorted_items[1] - sorted_items[0]
#     a = [(i + step) for i in range(len(sorted_items)+1)]
#     for i in a:
#         if i not in items:
#             return i
#
#
#
# print("Example:")
# print(missing_number([2, 6, 8]))
#
# # These "asserts" are used for self-checking
# assert missing_number([1, 4, 2, 5]) == 3
# assert missing_number([2, 6, 8]) == 4
# assert missing_number([5, 25, 30, 20, 15]) == 10
#
# # print("The mission is done! Click 'Check Solution' to earn rewards!")


# from collections import namedtuple
#
# Pawn = namedtuple('Pawn', "column row")
#
#
# def safe_pawns(pawns: set) -> int:
#     def is_safe(pawn, board):
#         return (Pawn(pawn.column - 1, pawn.row - 1) in board
#                 or Pawn(pawn.column + 1, pawn.row - 1) in board)
#
#     board = {Pawn(ord(column), ord(row)) for column, row in pawns}
#     return sum(1 for pawn in board if is_safe(pawn, board))
#
#
# print("Example:")
# print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
#
# assert safe_pawns({"f4", "d4", "e3", "b4", "g5", "d2", "c3"}) == 6
# assert safe_pawns({"f4", "c4", "b4", "e4", "g4", "d4", "e5"}) == 1
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def safe_pawns(pawns):
#     pawn_indexes = list()  # Координаты, данные в задаче, планируем хранить в списке
#     for i in pawns:  # Пробегаю по списку, перевожу координаты шахмат в цифровые значения
#         rows = int(i[1]) - 1
#         colums = (ord(i[0]) - 97)
#         pawn_indexes.append((colums, rows))
#
#     count = 0  # Создаю счетчик, где будет хранится кол-во найденных "диагоналей"
#     for j in pawn_indexes:
#         if pawn_indexes.count((j[0] - 1, j[1] - 1)) != 0:
#             count = count + (pawn_indexes.count((j[0] - 1, j[1] - 1)))
#         else:
#             count = count + (pawn_indexes.count((j[0] + 1, j[1] - 1)))
#     return count
#
#
# print("Example:")
# print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
#
# assert safe_pawns({"f4", "d4", "e3", "b4", "g5", "d2", "c3"}) == 6
# assert safe_pawns({"f4", "c4", "b4", "e4", "g4", "d4", "e5"}) == 1
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from typing import Iterable
#
#
# def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
#     return sorted(items, key=lambda x: (-items.count(x), items.index(x)))
#
#
# print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))
#
# # These "asserts" are used for self-checking
# assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
# assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
# assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
#     "bob",
#     "bob",
#     "bob",
#     "carl",
#     "alex",
# ]
# assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
# assert list(frequency_sort([])) == []
# assert list(frequency_sort([1])) == [1]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

#
# from typing import Union
# from datetime import datetime
#
#
# def sun_angle(time: str) -> Union[float, str]:
#     # dt = datetime.strptime(time, "%H:%M")
#     # up_sun = 6 * 60
#     # down_sun = 18 * 60
#     # minute_time = dt.time().hour * 60 + dt.time().minute
#     # if minute_time in range(up_sun, down_sun + 1):
#     #     return 180 * (minute_time - up_sun) / (down_sun - up_sun)
#     # else:
#     #     return f"I don't see the sun!"
#
#     try:
#         hour, minute = map(int, time.split(":"))
#         minute_time = hour * 60 + minute
#         if 6 * 60 <= minute_time <= 18 * 60:
#             return 180 * (minute_time - 6 * 60) / (18 * 60 - 6 * 60)
#         else:
#             raise ValueError("I don't see the sun!")
#     except ValueError as e:
#         return str(e)
#
#
# print(sun_angle("07:00"))
# assert sun_angle("07:00") == 15
# assert sun_angle("12:15") == 93.75
# assert sun_angle('18:01') == "I don't see the sun!"
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from typing import Any, Iterable
# from math import ceil
#
#
# def split_list(items: list[Any]) -> Iterable[list[Any]]:
#     # res = []
#     # first_part = ceil((len(items) / 2))
#     # a = items[:first_part]
#     # b = items[first_part:]
#     # res.append(a)
#     # res.append(b)
#     # return res
#
#     #or
#     middle = ceil((len(items) / 2))
#     return [items[:middle], items[middle:]]
#
#
#
# print("Example:")
# print(list(split_list([1, 2, 3, 4, 5, 6])))
#
# assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
# assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
# assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
#     ["banana", "apple", "orange"],
#     ["cherry", "watermelon"],
# ]
# assert list(split_list([1])) == [[1], []]
# assert list(split_list([])) == [[], []]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# import time as my_time
#
#
# def date_time(time: str) -> str:
#     time_parse = my_time.strptime(time, '%d.%m.%Y %H:%M')
#
#     day = time_parse.tm_mday
#     month = my_time.strftime("%B", time_parse)
#     year = time_parse.tm_year
#     hour = time_parse.tm_hour
#     minute = time_parse.tm_min
#
#     minute_str = "minute" if minute == 1 else "minutes"
#     hour_str = "hour" if hour == 1 else "hours"
#
#     return f"{day} {month} {year} year {hour} {hour_str} {minute} {minute_str}"
#
#
# print("Example:")
# print(date_time("11.04.1812 01:01"))
#
# assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
# assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"
# assert date_time('09.07.1995 16:01') == '9 July 1995 year 16 hours 1 minute'
# assert date_time('11.04.1812 01:01') == '11 April 1812 year 1 hour 1 minute'
# assert date_time('11.04.1812 01:01') == '11 April 1812 year 1 hour 1 minute'
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from time import strptime, strftime
#
#
# def date_time(time_str: str) -> str:
#     time_parse = strptime(time_str, '%d.%m.%Y %H:%M')
#
#     day, month, year, hour, minute = (time_parse.tm_mday,
#                                       strftime("%B", time_parse),
#                                       time_parse.tm_year,
#                                       time_parse.tm_hour,
#                                       time_parse.tm_min)
#
#     minute_str = "minute" if minute == 1 else "minutes"
#     hour_str = "hour" if hour == 1 else "hours"
#
#     return f"{day} {month} {year} year {hour} {hour_str} {minute} {minute_str}"
#
#
# print("Example:")
# print(date_time("11.04.1812 01:01"))
#
# assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
# assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"
# assert date_time('09.07.1995 16:01') == '9 July 1995 year 16 hours 1 minute'
# assert date_time('11.04.1812 01:01') == '11 April 1812 year 1 hour 1 minute'
# assert date_time('11.04.1812 01:01') == '11 April 1812 year 1 hour 1 minute'


# MORSE = {
#     ".-": "a",
#     "-...": "b",
#     "-.-.": "c",
#     "-..": "d",
#     ".": "e",
#     "..-.": "f",
#     "--.": "g",
#     "....": "h",
#     "..": "i",
#     ".---": "j",
#     "-.-": "k",
#     ".-..": "l",
#     "--": "m",
#     "-.": "n",
#     "---": "o",
#     ".--.": "p",
#     "--.-": "q",
#     ".-.": "r",
#     "...": "s",
#     "-": "t",
#     "..-": "u",
#     "...-": "v",
#     ".--": "w",
#     "-..-": "x",
#     "-.--": "y",
#     "--..": "z",
#     "-----": "0",
#     ".----": "1",
#     "..---": "2",
#     "...--": "3",
#     "....-": "4",
#     ".....": "5",
#     "-....": "6",
#     "--...": "7",
#     "---..": "8",
#     "----.": "9",
# }
#

# def morse_decoder(code: str) -> str:
#     # res = []
#     # words = code.split("   ")
#     # for word in words:
#     #     letters = word.split()
#     #     decoded = ""
#     #     for letter in letters:
#     #         decoded += MORSE[letter]
#     #     res.append(decoded)
#     # return " ".join(res).capitalize()
#
#     # or
#     decoded_words = ["".join(MORSE[letter] for letter in word.split()) for word in code.split("   ")]
#     return " ".join(decoded_words).capitalize()
#
#
# print("Example:")
# print(morse_decoder("... --- -- .   - . -..- -"))
#
# # These "asserts" are used for self-checking
# assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
# assert (
#     morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
#     == "I was born in 1990"
# )
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# # from typing import Iterable
# # def replace_last(line: list) -> Iterable:
# #     if len(line) == 0:
# #         return []
# #
# #     last_el = line.pop()
# #     line.insert(0, last_el)
# #     return line
#
# # or
# from collections import deque
# from typing import Iterable
#
#
# def replace_last(line: list) -> Iterable:
#     if not line:
#         return []
#
#     dq = deque(line)
#     dq.rotate(1)
#     return list(dq)
#
#
# print("Example:")
# print(list(replace_last([2, 3, 4, 1])))
#
# assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
# assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
# assert list(replace_last([1])) == [1]
# assert list(replace_last([])) == []
#
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def index_power(ar: list[int], n: int) -> int:
#     # if n > len(ar) - 1:
#     #     return -1
#     # return ar[n]**n
#
#     # or
#     try:
#         return ar[n] ** n
#     except IndexError:
#         return -1
#
#
# print("Example:")
# print(index_power([1, 2, 3], 2))
#
# # These "asserts" are used for self-checking
# assert index_power([1, 2, 3, 4], 2) == 9
# assert index_power([1, 3, 10, 100], 3) == 1000000
# assert index_power([0, 1], 0) == 1
# assert index_power([1, 2], 3) == -1
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

from collections import Counter


# def is_majority(items: list[bool]) -> bool:
#     if not items:
#         return False
#     return items.count(True) > len(items) / 2
#
#
#
#
# print("Example:")
# print(is_majority([True, True, False, False]))
#
# # These "asserts" are used for self-checking
# assert is_majority([True, True, False, True, False]) == True
# assert is_majority([True, True, False]) == True
# assert is_majority([True, True, False, False]) == False
# assert is_majority([True, True, False, False, False]) == False
# assert is_majority([False]) == False
# assert is_majority([True]) == True
# assert is_majority([]) == False
# assert is_majority([False, False, True]) == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def checkio(values: list) -> list:
#     return sorted(values, key=abs)
#
#
# print("Example:")
# print(checkio([-20, -5, 10, 15]))
#
# # These "asserts" are used for self-checking
# assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
# assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
# assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def count_vowels(text: str) -> int:
#     # count = 0
#     # for letter in text.lower():
#     #     if letter in ("a", "e", "i", "o", "u"):
#     #         count += 1
#     # return count
#
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     return sum(text.lower().count(vowel) for vowel in vowels)
#
#
#
# print("Example:")
# print(count_vowels("Hello"))
#
# # These "asserts" are used for self-checking
# assert count_vowels("hello") == 2
# assert count_vowels("openai") == 4
# assert count_vowels("typescript") == 2
# assert count_vowels("a") == 1
# assert count_vowels("b") == 0
# assert count_vowels("aeiou") == 5
# assert count_vowels("AEIOU") == 5
# assert count_vowels("The quick brown fox") == 5
# assert count_vowels("Jumps over the lazy dog") == 6
# assert count_vowels("") == 0
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def to_title_case(sentence: str) -> str:
#     return sentence.title()
#
#
# print("Example:")
# print(to_title_case("hello world"))
#
# # These "asserts" are used for self-checking
# assert to_title_case("hello world") == "Hello World"
# assert to_title_case("openai gpt-4") == "Openai Gpt-4"
# assert to_title_case("this is a title") == "This Is A Title"
# assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
# assert to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog"
# assert to_title_case("typescript is great") == "Typescript Is Great"
# assert to_title_case("the answer is 42") == "The Answer Is 42"
# assert to_title_case("to be or not to be") == "To Be Or Not To Be"
# assert to_title_case("that is the question") == "That Is The Question"
# assert to_title_case("") == ""
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from datetime import datetime
# from typing import List
#
#
# def sum_light(els: List[datetime]) -> int:
#     """
#     how long the light bulb has been turned on
#     """
#     total_light = 0
#     for i in range(0, len(els), 2):
#         total_light += (els[i + 1] - els[i]).total_seconds()
#     return int(total_light)
#
#
# if __name__ == "__main__":
#     print("Example:")
#     print(
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#             ]
#         )
#     )
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert (
#             sum_light(
#                 els=[
#                     datetime(2015, 1, 12, 10, 0, 0),
#                     datetime(2015, 1, 12, 10, 10, 10),
#                 ]
#             )
#             == 610
#     )
#
#     assert (
#             sum_light(
#                 [
#                     datetime(2015, 1, 12, 10, 0, 0),
#                     datetime(2015, 1, 12, 10, 10, 10),
#                     datetime(2015, 1, 12, 11, 0, 0),
#                     datetime(2015, 1, 12, 11, 10, 10),
#                 ]
#             )
#             == 1220
#     )
#
#     assert (
#             sum_light(
#                 [
#                     datetime(2015, 1, 12, 10, 0, 0),
#                     datetime(2015, 1, 12, 10, 10, 10),
#                     datetime(2015, 1, 12, 11, 0, 0),
#                     datetime(2015, 1, 12, 11, 10, 10),
#                     datetime(2015, 1, 12, 11, 10, 10),
#                     datetime(2015, 1, 12, 12, 10, 10),
#                 ]
#             )
#             == 4820
#     )
#
#     assert (
#             sum_light(
#                 [
#                     datetime(2015, 1, 12, 10, 0, 0),
#                     datetime(2015, 1, 12, 10, 0, 1),
#                 ]
#             )
#             == 1
#     )
#
#     assert (
#             sum_light(
#                 [
#                     datetime(2015, 1, 12, 10, 0, 0),
#                     datetime(2015, 1, 12, 10, 0, 10),
#                     datetime(2015, 1, 12, 11, 0, 0),
#                     datetime(2015, 1, 13, 11, 0, 0),
#                 ]
#             )
#             == 86410
#     )
#
#     print(
#         "The first mission in series is completed? Click 'Check' to earn cool rewards!"
#     )


# from collections.abc import Iterable
#
#
# def remove_all_after(items: list[int], border: int) -> Iterable[int]:
#     # try:
#     #     if len(items) == 0: return []
#     #     if items.index(border) == ValueError: raise ValueError
#     # except ValueError:
#     #     return items
#     #
#     # return items[:items.index(border) + 1]
#
#     # or
#     if not items:
#         return []
#
#     try:
#         index = items.index(border)
#     except ValueError:
#         return items
#
#     return items[:index + 1]
#
#
# print("Example:")
# print(list(remove_all_after([1, 2, 3, 4, 5], 3)))
#
# # These "asserts" are used for self-checking
# assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
# assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
# assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
# assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
# assert list(remove_all_after([], 0)) == []
# assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# Taken from mission Lightbulb Intro

# from datetime import datetime
# from typing import List, Optional
#
#
# def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
#     """
#     how long the light bulb has been turned on
#     """
#     total_light = 0
#
#     for i in range(0, len(els), 2):
#         light_on_time = (els[i + 1] - els[i]).total_seconds()
#
#         if start_watching:
#             if start_watching >= els[i + 1]:
#                 continue
#             elif start_watching > els[i]:
#                 light_on_time -= (start_watching - els[i]).total_seconds()
#
#         total_light += max(light_on_time, 0)
#
#     return int(total_light)
#
#
# if __name__ == "__main__":
#     print("Example:")
#     print(
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 0, 10),
#             ],
#             datetime(2015, 1, 12, 10, 0, 5),
#         )
#     )
#
#     assert (
#         sum_light(
#             els=[
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 0, 10),
#             ],
#             start_watching=datetime(2015, 1, 12, 10, 0, 5),
#         )
#         == 5
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 0, 10),
#             ],
#             datetime(2015, 1, 12, 10, 0, 0),
#         )
#         == 10
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#             ],
#             datetime(2015, 1, 12, 11, 0, 0),
#         )
#         == 610
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#             ],
#             datetime(2015, 1, 12, 11, 0, 10),
#         )
#         == 600
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#             ],
#             datetime(2015, 1, 12, 10, 10, 0),
#         )
#         == 620
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#                 datetime(2015, 1, 12, 11, 10, 11),
#                 datetime(2015, 1, 12, 12, 10, 11),
#             ],
#             datetime(2015, 1, 12, 12, 10, 11),
#         )
#         == 0
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#                 datetime(2015, 1, 12, 11, 10, 11),
#                 datetime(2015, 1, 12, 12, 10, 11),
#             ],
#             datetime(2015, 1, 12, 12, 9, 11),
#         )
#         == 60
#     )
#
#     print("The second mission in series is done? Click 'Check' to earn cool rewards!")


# import statistics
#
#
# def median(data: list[int]) -> int | float:
#     return statistics.median(data)
#
#
# print("Example:")
# print(median([3, 6, 20, 99, 10, 15]))
#
# # These "asserts" are used for self-checking
# assert median([1, 2, 3, 4, 5]) == 3
# assert median([3, 1, 2, 5, 3]) == 3
# assert median([1, 300, 2, 200, 1]) == 2
# assert median([3, 6, 20, 99, 10, 15]) == 12.5
# assert median([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
# assert median([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
# assert median([33, 56, 62]) == 56
# assert median([21, 56, 84, 82, 52, 9]) == 54
# assert median([100, 1, 1, 1, 1, 1, 1]) == 1
# assert median([64, 6, 92, 7, 70, 5]) == 35.5
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def correct_sentence(text: str) -> str:
#     # if text.endswith("."):
#     #     return text.capitalize()
#     # else:
#     #     return text.capitalize() + "."
#
#     return (text[0].upper()+text[1:]) if text.endswith(".") else (text[0].upper()+text[1:] + ".")
#
#
# print("Example:")
# print(correct_sentence("welcome to New York"))
#
# # These "asserts" are used for self-checking
# assert correct_sentence("greetings, friends") == "Greetings, friends."
# assert correct_sentence("Greetings, friends") == "Greetings, friends."
# assert correct_sentence("Greetings, friends.") == "Greetings, friends."
# assert correct_sentence("greetings, friends.") == "Greetings, friends."
# assert correct_sentence('welcome to New York') == 'Welcome to New York.'
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def words_order(text: str, words: list) -> bool:
#     # if len(words) != len(set(words)):
#     #     return False
#     # words_in_text = text.split()
#     # indices = []
#     # for word in words:
#     #     if word not in words_in_text:
#     #         return False
#     #     indices.append(words_in_text.index(word))
#     # return indices == sorted(indices)
#
#     # or
#     # Проверка наличия повторяющихся слов в списке
#     if len(words) != len(set(words)):
#         return False
#     words_in_text = text.split()
#     # Проверяем, что все слова из words присутствуют в words_in_text
#     if not all(word in words_in_text for word in words):
#         return False
#     # Получаем индексы слов в тексте
#     indices = [words_in_text.index(word) for word in words]
#     return indices == sorted(indices)
#
#
# print("Example:")
# print(words_order("hi world im here", ["world", "here"]))
#
# # These "asserts" are used for self-checking
# assert words_order("hi world im here", ["world", "here"]) == True
# assert words_order("hi world im here", ["here", "world"]) == False
# assert words_order("hi world im here", ["world"]) == True
# assert words_order("hi world im here", ["world", "here", "hi"]) == False
# assert words_order("hi world im here", ["world", "im", "here"]) == True
# assert words_order("hi world im here", ["world", "hi", "here"]) == False
# assert words_order("hi world im here", ["world", "world"]) == False
# assert words_order("hi world im here", ["country", "world"]) == False
# assert words_order("hi world im here", ["wo", "rld"]) == False
# assert words_order("", ["world", "here"]) == False
# assert words_order("hi world world im here", ["world", "world"]) == False
# assert (
#         words_order("hi world world im here hi world world im here", ["world", "here"])
#         == True
# )
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def replace_all(mainText: str, target: str, repl: str) -> str:
#     # your code here
#     return mainText.replace(target, repl)
#
#
# print("Example:")
# print(replace_all("hello world", "world", "TypeScript"))
#
# # These "asserts" are used for self-checking
# assert replace_all("hello world", "world", "TypeScript") == "hello TypeScript"
# assert (
#     replace_all("hello world world", "world", "TypeScript")
#     == "hello TypeScript TypeScript"
# )
# assert replace_all("TypeScript is fun", "fun", "awesome") == "TypeScript is awesome"
# assert replace_all("aaa", "a", "b") == "bbb"
# assert replace_all("replace all the all", "all", "some") == "replace some the some"
# assert replace_all("nothing to replace", "something", "nothing") == "nothing to replace"
# assert replace_all("same same same", "same", "same") == "same same same"
# assert replace_all("123 123", "123", "321") == "321 321"
# assert replace_all("OpenAI", "AI", "Source") == "OpenSource"
# assert replace_all("", "anything", "nothing") == ""
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# from datetime import datetime
# def time_converter(time: str) -> str:
#     return datetime\
#         .strptime(time, '%H:%M').strftime('%I:%M %p')\
#         .lstrip('0').lower().replace('m', '.m.')

# or
# from time import strptime
# from datetime import time
#
# time_converter = lambda t: (time(*strptime(t, '%H:%M')[3:5]).strftime('%I:%M %p')
#                             .lstrip('0').lower().replace('m', '.m.'))
#
# if __name__ == '__main__':
#     print("Example:")
#     print(time_converter("12:30"))
#
#     assert time_converter("12:30") == "12:30 p.m."
#     assert time_converter("09:00") == "9:00 a.m."
#
#     print("The mission is done! Click 'Check Solution' to earn rewards!")


# def goes_after(word: str, first: str, second: str) -> bool:
#     first_index, second_index = word.find(first), word.find(second)
#     return first_index != -1 and second_index != -1 and second_index == first_index + 1
#
#
# print("Example:")
# print(goes_after('almaz', 'm', 'a'))
#
# # These "asserts" are used for self-checking
# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("panorama", "a", "n") == True
# assert goes_after("list", "l", "o") == False
# assert goes_after("", "l", "o") == False
# assert goes_after("list", "l", "l") == False
# assert goes_after("world", "d", "w") == False
# assert goes_after("Almaz", "a", "l") == False
# assert goes_after('transport', 'r', 't') == False
# assert goes_after('almaz', 'm', 'a') == False
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def sum_digits(num: int) -> int:
#     my_num = str(num)
#     if len(my_num) == 1:
#         return int(num)
#
#     res = 0
#     for i in my_num:
#         res += int(i)
#
#     while res >= 10:
#         res = sum(int(digit) for digit in str(res))
#
#     return res
#
#
# print("Example:")
# print(sum_digits(38))
#
# # These "asserts" are used for self-checking
# assert sum_digits(38) == 2
# assert sum_digits(0) == 0
# assert sum_digits(10) == 1
# assert sum_digits(132) == 6
# assert sum_digits(232) == 7
# assert sum_digits(811) == 1
# assert sum_digits(702) == 9
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from collections.abc import Iterable
# from collections import deque
#
#
# def except_zero(items: list[int]) -> Iterable[int]:
#     # zero_positions = [index for index, value in enumerate(items) if value == 0]
#     # sorted_items = sorted(item for item in items if item != 0)
#     # for position in zero_positions:
#     #     sorted_items.insert(position, 0)
#     # return sorted_items
#
#     # or
#     zero_positions = [index for index, value in enumerate(items) if value == 0]
#     non_zero_sorted = sorted(filter(lambda x: x != 0, items))
#     sorted_items = deque(non_zero_sorted)
#     for position in zero_positions:
#         sorted_items.insert(position, 0)
#     return list(sorted_items)
#
#
# print("Example:")
# print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))
#
# # These "asserts" are used for self-checking
# assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
# assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
# assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
# assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
# assert list(except_zero([0, 0])) == [0, 0]
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from collections.abc import Iterable
# from collections import Counter
#
#
# def frequency_sorting(numbers: list[int]) -> Iterable[int]:
#     counts = Counter(numbers)
#     return sorted(numbers, key=lambda x: (-counts[x], x))
#
#
# print("Example:")
# print(list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])))
#
# # These "asserts" are used for self-checking
# assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
# assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
#     4,
#     4,
#     4,
#     3,
#     3,
#     11,
#     11,
#     7,
#     13,
# ]
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# from datetime import datetime
#
#
# def time_converter(time):
#     time = time.replace("a.m.", "AM").replace("p.m.", "PM")
#     return datetime.strptime(time, "%I:%M %p").strftime("%H:%M")
#
#
# if __name__ == "__main__":
#     print("Example:")
#     print(time_converter("12:30 p.m."))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert time_converter("12:30 p.m.") == "12:30"
#     assert time_converter("9:00 a.m.") == "09:00"
#     assert time_converter("11:15 p.m.") == "23:15"
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# # def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
# #     if len(items) == 0:
# #         return ["", 0]
# #     first = ""
# #     second = 0
# #     for i in items:
# #         if type(i) == int:
# #             second += i
# #         elif type(i) == str:
# #             first += i
# #     return [first, second]
# # or
# from typing import Union, List
#
#
# def sum_by_types(items: List[Union[str, int]]) -> Union[tuple[str, int], list[str, int]]:
#     string_sum = ''.join(str(item) for item in items if isinstance(item, str))
#     int_sum = sum(item for item in items if isinstance(item, int))
#     return [string_sum, int_sum] if string_sum else ("", int_sum)
#
#
# print("Example:")
# print(list(sum_by_types([1, 2, 3])))
#
# assert list(sum_by_types([])) == ["", 0]
# assert list(sum_by_types([1, 2, 3])) == ["", 6]
# assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
# assert list(sum_by_types(["1", "2", 3])) == ["12", 3]
# assert list(sum_by_types(["1", "2", "3"])) == ["123", 0]
# assert list(sum_by_types(["size", 12, "in", 45, 0])) == ["sizein", 57]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def longest_substr(s: str) -> int:
#     char_set = set()
#     max_length = 0
#     left_ptr = 0
#
#     for right_ptr in range(len(s)):
#         while s[right_ptr] in char_set:
#             char_set.remove(s[left_ptr])
#             left_ptr += 1
#         char_set.add(s[right_ptr])
#         max_length = max(max_length, right_ptr - left_ptr + 1)
#
#     return max_length
#
#
# print("Example:")
# print(longest_substr("pwwkew"))
#
# # These "asserts" are used for self-checking
# assert longest_substr("abcabcbb") == 3
# assert longest_substr("bbbbb") == 1
# assert longest_substr("pwwkew") == 3
# assert longest_substr("abcdef") == 6
# assert longest_substr("") == 0
# assert longest_substr("au") == 2
# assert longest_substr("dvdf") == 3
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def translation(text: str) -> str:
#     vowels = "aeiouy"
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i] != ' ':
#             result += text[i]
#             if text[i] not in vowels:
#                 i += 2
#             else:
#                 i += 3
#         else:
#             result += ' '
#             i += 1
#     return result.strip()
#
#
# print("Example:")
# print(translation("hoooowe yyyooouuu duoooiiine"))
#
# # These "asserts" are used for self-checking
# assert translation("hieeelalaooo") == "hello"
# assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
# assert translation("aaa bo cy da eee fe") == "a b c d e f"
# assert translation("sooooso aaaaaaaaa") == "sos aaa"
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def checkio(line1: str, line2: str) -> str:
#     # list_1, list_2, res = line2.split(","), line1.split(","), []
#     # for element in list_1:
#     #     if element in list_2:
#     #         res.append(element)
#     # res = sorted(res)
#     # return ",".join(res)
#
#     # or
#     return ",".join(sorted(set(line1.split(",")).intersection(set(line2.split(",")))))
#
#
# print("Example:")
# print(checkio("one,two,three", "four,five,one,two,six,three"))
#
# # These "asserts" are used for self-checking
# assert checkio("hello,world", "hello,earth") == "hello"
# assert checkio("one,two,three", "four,five,six") == ""
# assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# import datetime as dt
#
#
# def get_latest(dt1str: str, dt2str: str) -> str:
#     dt_1 = dt.datetime.strptime(dt1str, "%Y-%m-%dT%H:%M:%S")
#     dt_2 = dt.datetime.strptime(dt2str, "%Y-%m-%dT%H:%M:%S")
#     return dt1str if dt_1 > dt_2 else dt2str if dt_1 == dt_2 else dt2str
#
#     # if dt_1 > dt_2:
#     #     return dt1str
#     # elif dt_1 == dt_2:
#     #     return dt2str
#     # else:
#     #     return dt2str
#
#
# print("Example:")
# print(get_latest("0001-01-01T01:01:01", "3000-11-16T13:27:02"))
#
# assert get_latest("2007-03-04T21:08:12", "2007-03-04T21:08:12") == "2007-03-04T21:08:12"
# assert get_latest("2027-09-01T01:03:10", "1997-04-15T11:18:14") == "2027-09-01T01:03:10"
# assert get_latest("0001-01-01T01:01:01", "3000-11-16T13:27:02") == "3000-11-16T13:27:02"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def count_occurrences(main_str: str, sub_str: str) -> int:
#     l_main_str, l_sub_str = main_str.lower(), sub_str.lower()
#     return sum(1 for i in range(len(l_main_str) - len(l_sub_str) + 1)
#                if l_main_str[i:i+len(l_sub_str)] == l_sub_str)
#
#
# print("Example:")
# print(count_occurrences("hello world hello", "hello"))
#
# # These "asserts" are used for self-checking
# assert count_occurrences("hello world hello", "hello") == 2
# assert count_occurrences("Hello World hello", "hello") == 2
# assert count_occurrences("hello", "world") == 0
# assert count_occurrences("hello world hello world hello", "world") == 2
# assert count_occurrences("HELLO", "hello") == 1
# assert count_occurrences("appleappleapple", "appleapple") == 2
# assert count_occurrences("HELLO WORLD", "WORLD") == 1
# assert count_occurrences("hello world hello", "o w") == 1
# assert count_occurrences("apple apple apple", "apple") == 3
# assert count_occurrences("apple Apple apple", "apple") == 3
# assert count_occurrences("apple", "APPLE") == 1
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# # Буква «f» - указывает на то, что Вам нужно двигаться вперед, «b» - назад, «l» - влево, а «r» - вправо.
# def follow(instructions: str) -> tuple[int, int] | list[int]:
#     # res = [0, 0]
#     # for instruction in instructions:
#     #     match instruction:
#     #         case "f":
#     #             res[1] += 1
#     #         case "b":
#     #             res[1] -= 1
#     #         case "l":
#     #             res[0] -= 1
#     #         case "r":
#     #             res[0] += 1
#     # return res
#
#     # or
#     movements = {"f": (0, 1), "b": (0, -1), "l": (-1, 0), "r": (1, 0)}
#     x, y = 0, 0
#     for instruction in instructions:
#         move = movements.get(instruction)
#         if move:
#             dx, dy = move
#             x += dx
#             y += dy
#     return x, y
#
#
# print("Example:")
# print(list(follow("ffrff")))
#
# # These "asserts" are used for self-checking
# assert list(follow("fflff")) == [-1, 4]
# assert list(follow("ffrff")) == [1, 4]
# assert list(follow("fblr")) == [0, 0]
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def check_pangram(text: str) -> bool:
#     return not set("abcdefghijklmnopqrstuvwxyz").difference(set(text.lower()))
#
#
# print("Example:")
# print(check_pangram("The quick brown fox jumps over the lazy dog."))
#
# # These "asserts" are used for self-checking
# assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
# assert check_pangram("ABCDEF") == False
# assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
# assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
# assert check_pangram("abcdefghijklmnopqrstuvwxy") == False
# assert (
#         check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
#         == True
# )
# assert check_pangram("As quirky joke, chefs won't pay devil magic zebra tax.") == True
# assert check_pangram("Six big devils from Japan quickly forgot how to walt.") == False
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def checkio(*args):
#     return 0 if len(args) == 0 else max(args) - min(args)
#
#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     def almost_equal(checked, correct, significant_digits):
#         precision = 0.1 ** significant_digits
#         return correct - precision < checked < correct + precision
#
#
#     print('Example:')
#     print(checkio(1, 2, 3))
#
#     assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
#     assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
#     assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
#     assert almost_equal(checkio(), 0, 3), "Empty"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# import re
#
#
# def find_quotes(a):
#     return re.findall(r'"([^"]*)"', a)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(find_quotes('good morning mister "superman"'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert find_quotes('"Greetings"') == ['Greetings']
#     assert find_quotes('Hi') == []
#     assert find_quotes('good morning mister "superman"') == ['superman']
#     assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
#     assert find_quotes('"Lorem Ipsum" is simply dummy text '
#                        'of the printing and typesetting '
#                        'industry. Lorem Ipsum has been the '
#                        '"industry\'s standard dummy text '
#                        'ever since the 1500s", when an '
#                        'unknown printer took a galley of '
#                        'type and scrambled it to make a type '
#                        'specimen book. It has survived not '
#                        'only five centuries, but also the '
#                        'leap into electronic typesetting, '
#                        'remaining essentially unchanged. "It '
#                        'was popularised in the 1960s" with '
#                        'the release of Letraset sheets '
#                        'containing Lorem Ipsum passages, and '
#                        'more recently with desktop '
#                        'publishing software like Aldus '
#                        'PageMaker including versions of '
#                        'Lorem Ipsum.') == ['Lorem Ipsum',
#                                            "industry's standard dummy text ever "
#                                            'since the 1500s',
#                                            'It was popularised in the 1960s']
#     assert find_quotes('count empty quotes ""') == ['']
#     print("Coding complete? Click 'Check' to earn cool rewards!")


#
# def beat_previous(digits: str) -> list[int]:
#     result, current_num = [], ""
#     for digit in digits:
#         current_num += digit
#         if not result or int(current_num) > result[-1]:
#             result.append(int(current_num))
#             current_num = ''
#     return result
#
#
# print("Example:")
# print(beat_previous("77777777777777777777777"))
#
# # These "asserts" are used for self-checking
# assert beat_previous("600005") == [6]
# assert beat_previous("6000050") == [6, 50]
# assert beat_previous("045349") == [0, 4, 5, 34]
# assert beat_previous("77777777777777777777777") == [7, 77, 777, 7777, 77777, 777777]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# from collections import Counter
#
#
# def checkio(text: str) -> str:
#     often_used = Counter(filter(str.isalpha, text.lower()))
#     return max(often_used, key=lambda x: (often_used[x], -ord(x)))
#
#
#
# print("Example:")
# print(checkio("Hello World!"))
#
# # These "asserts" are used for self-checking
# assert checkio("Hello World!") == "l"
# assert checkio("How do you do?") == "o"
# assert checkio("One") == "e"
# assert checkio("Oops!") == "o"
# assert checkio("AAaooo!!!!") == "a"
# assert checkio("abe") == "a"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def is_number(val: str) -> bool:
#     return val.isdigit()
#
#
# print("Example:")
# print(is_number("34"))
#
# # These "asserts" are used for self-checking
# assert is_number("34") == True
# assert is_number("df") == False
# assert is_number("") == False
# assert is_number("a5") == False
# assert is_number("ITS A NUMBER") == False
# assert is_number("5a") == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from typing import Iterable
#
#
# def move_zeros(items: list[int]) -> Iterable[int]:
#     items.sort(reverse=True, key=bool)
#     return items
#
#
# print("Example:")
# print(list(move_zeros([0, 1, 0, 3, 12])))
#
# # These "asserts" are used for self-checking
# assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
# assert list(move_zeros([0])) == [0]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# from itertools import groupby
#
#
# def long_repeat(line: str) -> int:
#     # if not line:
#     #     return 0
#     #
#     # max_repeat = 1
#     # current_repeat = 1
#     #
#     # for i in range(1, len(line)):
#     #     if line[i] == line[i-1]:
#     #         current_repeat += 1
#     #         max_repeat = max(max_repeat, current_repeat)
#     #     else:
#     #         current_repeat = 1
#     # return max_repeat
#
#     # or
#     return max((sum(1 for _ in g) for _, g in groupby(line)), default=0)
#
#
# print("Example:")
# print(long_repeat("sdsffffse"))
#
# assert long_repeat("sdsffffse") == 4
# assert long_repeat("ddvvrwwwrggg") == 3
# assert long_repeat('') == 0
# assert long_repeat('abababaab') == 2
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# from typing import List, Tuple
#
#
# def is_intersecting(circle1, circle2):
#     x1, y1, r1 = circle1
#     x2, y2, r2 = circle2
#     distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
#     return (r1 + r2) ** 2 > distance_squared > (r2 - r1) ** 2
#
#
# def dfs(node, graph, visited):
#     visited.add(node)
#     for neighbor, intersect in enumerate(graph[node]):
#         if intersect and neighbor not in visited:
#             dfs(neighbor, graph, visited)
#
#
# def count_chains(circles: List[Tuple[int, int, int]]) -> int:
#     n = len(circles)
#     graph = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(i + 1, n):
#             if is_intersecting(circles[i], circles[j]):
#                 graph[i][j] = graph[j][i] = 1
#
#     visited = set()
#     chains = 0
#     for i in range(n):
#         if i not in visited:
#             dfs(i, graph, visited)
#             chains += 1
#
#     return chains
#
# # # or1
# # import networkx as nx
# # from itertools import combinations
# # from typing import List, Tuple
# #
# #
# # def count_chains(circles: List[Tuple[int, int, int]]) -> int:
# #     G = nx.Graph()
# #     G.add_nodes_from(range(len(circles)))
# #
# #     for (i, circle1), (j, circle2) in combinations(enumerate(circles), 2):
# #         x1, y1, r1 = circle1
# #         x2, y2, r2 = circle2
# #         distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
# #         if (r1 + r2) ** 2 > distance_squared > (r2 - r1) ** 2:
# #             G.add_edge(i, j)
# #
# #     return nx.number_connected_components(G)
#
# # # or2
# # from typing import List, Tuple
# # import math
# #
# #
# # def count_chains(circles: List[Tuple[int, int, int]]) -> int:
# #     def is_intersecting(circle1, circle2):
# #         (x1, y1, r1), (x2, y2, r2) = circle1, circle2
# #         distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# #         return r1 + r2 > distance > abs(r1 - r2)
# #
# #     def dfs(node):
# #         visited.add(node)
# #         [dfs(neighbor) for neighbor, intersect in enumerate(graph[node]) if intersect and neighbor not in visited]
# #
# #     n = len(circles)
# #     graph = [[0] * n for _ in range(n)]
# #
# #     for i, circle1 in enumerate(circles):
# #         for j, circle2 in enumerate(circles[i + 1:], start=i + 1):
# #             if is_intersecting(circle1, circle2):
# #                 graph[i][j] = graph[j][i] = 1
# #
# #     visited = set()
# #     chains = sum(1 for i in range(n) if i not in visited and not dfs(i))
# #     return chains
#
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
#     assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
#     assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
#     assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
#     assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
#     assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
#     assert count_chains([(1, 3, 1), (2, 2, 1), (4, 2, 1), (5, 3, 1), (3, 3, 1)]) == 1
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# from pathlib import Path
# import os
#
#
# def sort_by_ext(files: list[str]) -> list[str]:
#     # def key_function(file):
#     #     parts = file.split('.')
#     #     if len(parts) == 1 or (len(parts) == 2 and parts[0] == ''):
#     #         return '', file
#     #     elif len(parts) == 2:
#     #         return parts[1], parts[0]
#     #     else:
#     #         return parts[-1], '.'.join(parts[:-1])
#     #
#     # return sorted(files, key=key_function)
#
#     # or1
#     # def key_function(file):
#     #     parts = file.split('.')
#     #     base_name = parts.pop(0) if parts[0] == '' else parts[0]
#     #     return parts[-1] if len(parts) > 1 else '', base_name
#     #
#     # return sorted(files, key=key_function)
#
#     # or2
#     # def key_function(file):
#     #     parts = file.split('.')
#     #     base_name = parts.pop(0) if parts[0] == '' else parts[0]
#     #     return parts[-1] if len(parts) > 1 else '', base_name
#     #
#     # return sorted(files, key=lambda file: key_function(Path(file).name)[0])
#
#     # or3
#     def key_function(file):
#         base_name, extension = os.path.splitext(file)
#         return extension, base_name
#
#     return sorted(files, key=lambda file: key_function(file)[0])
#
#
# print("Example:")
# print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))
#
# # These "asserts" are used for self-checking
# assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
#     "1.aa",
#     "1.bat",
#     "2.bat",
#     "1.cad",
# ]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
#     ".bat",
#     "1.aa",
#     "1.bat",
#     "1.cad",
# ]
# assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
#     ".aa",
#     ".bat",
#     "1.bat",
#     "1.cad",
# ]
# assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
#     "1.aa",
#     "1.bat",
#     "1.cad",
#     "1.aa.doc",
# ]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
#     "1.aa",
#     "1.bat",
#     "1.cad",
#     ".aa.doc",
# ]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

#
# from math import prod
#
#
# def checkio(number: int) -> int:
#     return prod([int(num) for num in str(number) if num != "0"])
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(checkio(123405))
#
#     # These "asserts" are used for self-checking
#     assert checkio(123405) == 120
#     assert checkio(999) == 729
#     assert checkio(1000) == 1
#     assert checkio(1111) == 1
#
#     print("The mission is done! Click 'Check Solution' to earn rewards!")


# import re
#
#
# def is_number(val: str) -> bool:
#     # return bool(re.match(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$',
#     #                      val.strip())) and 'e' not in val.lower()
#
#     # or
#     r = [i for i in val]
#     if (not val or any(c in ('+', '-') for c in r[1:])
#             or any(s.isalpha() for s in r[1:])
#             or (val.startswith(".") and len(val) == 1)):
#         return False
#     else:
#         return True
#
#
# print("Example:")
# print(is_number("1000"))
#
# # These "asserts" are used for self-checking
# assert is_number("34") == True
# assert is_number("df") == False
# assert is_number("") == False
# assert is_number("+10.0") == True
# assert is_number("1OOO") == False
# assert is_number("1.") == True
# assert is_number("+.l") == False
# assert is_number("++1+.2-") == False
# assert is_number("3e4") == False
# assert is_number('.') == False
# assert is_number('.1') == True
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def checkio(food: int) -> int:
#     fed = 0
#     new = 1
#     while food >= fed + new:
#         fed += new
#         food -= fed
#         new += 1
#     return max(food, fed)
#
#
# print("Example:")
# print(checkio(18))
#
# # These "asserts" are used for self-checking
# assert checkio(1) == 1
# assert checkio(3) == 2
# assert checkio(5) == 3
# assert checkio(10) == 6
# assert checkio(18) == 8
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# import calendar
#
#
# def checkio(year: int) -> int:
#     return sum(calendar.weekday(year, m, 13) == 4 for m in range(1, 13))
#
#
# if __name__ == "__main__":
#     print("Example:")
#     print(checkio(2015))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(2015) == 3, "First - 2015"
#     assert checkio(1986) == 1, "Second - 1986"
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# from typing import Iterable, Any
# from collections import defaultdict
#
#
# def remove_after_kth(items: list[Any], k: int) -> Iterable[Any]:
#     # if k <= 0:
#     #     return []
#     #
#     # count_map = {}
#     # result = []
#     #
#     # for item in items:
#     #     count_map[item] = count_map.get(item, 0) + 1
#     #     if count_map[item] <= k:
#     #         result.append(item)
#     #
#     # return result
#
#     # or
#     count_map = defaultdict(int)
#     return [item for item in items if
#             count_map[item] < k and not (count_map.update({item: count_map[item] + 1}) or False)]
#
#
# print("Example:")
# print(list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)))
#
# # These "asserts" are used for self-checking
# assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
# assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
# assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def is_acceptable_password(password: str) -> bool:
#     if len(set(password)) < 3:
#         return False
#     elif "password" in password.lower():
#         return False
#     elif len(password) >= 6 and any(letter.isdigit() for letter in password) and not password.isdigit():
#         return True
#     elif len(password) > 9:
#         return True
#     else:
#         return False
#
#
# print("Example:")
# print(is_acceptable_password("aaaaaa1"))
# # These "asserts" are used for self-checking
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False
# assert is_acceptable_password("muchlonger5") == True
# assert is_acceptable_password("sh5") == False
# assert is_acceptable_password("1234567") == False
# assert is_acceptable_password("12345678910") == True
# assert is_acceptable_password("password12345") == False
# assert is_acceptable_password("PASSWORD12345") == False
# assert is_acceptable_password("pass1234word") == True
# assert is_acceptable_password("aaaaaa1") == False
# assert is_acceptable_password("aaaaaabbbbb") == False
# assert is_acceptable_password("aaaaaabb1") == True
# assert is_acceptable_password("abc1") == False
# assert is_acceptable_password("abbcc12") == True
# assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def is_all_upper(text: str) -> bool:
#     return False if len(text.strip()) == 0 or text.isdigit() else text.isupper()
#
#
# print("Example:")
# print(is_all_upper("123 456"))
#
# # These "asserts" are used for self-checking
# assert is_all_upper("ALL UPPER") == True
# assert is_all_upper("all lower") == False
# assert is_all_upper("mixed UPPER and lower") == False
# assert is_all_upper("") == False
# assert is_all_upper('     ') == False
# assert is_all_upper('123') == False
# assert is_all_upper('123 456') == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# import re
#
#
# def from_camel_case(name: str) -> str:
#     name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
#     return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
#
#
# print("Example:")
# print(from_camel_case("IPhone"))
# # These "asserts" are used for self-checking
# assert from_camel_case("MyFunctionName") == "my_function_name"
# assert from_camel_case("IPhone") == "i_phone"
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# class LovePython:
#     def __init__(self):
#         self.feelings = ["excitement", "inspiration", "amazement"]
#         self.reasons = [
#             "Python is a simple and understandable language that makes programming fascinating.",
#             "A large number of libraries and frameworks make Python an ideal choice for various tasks.",
#             "Readable Python syntax makes the code understandable and easily maintainable.",
#             "Python has an extensive community ready to help and support in any matter.",
#             "A multitude of opportunities for automating routine tasks make life easier and more exciting.",
#             "The beautiful philosophy of Python, based on clarity and simplicity, aligns with my views on coding."
#         ]
#
#     @classmethod
#     def express_love(cls):
#         print("Why I love Python:")
#         for reason in cls().reasons:
#             print("-", reason)
#         print("Every time I write code in Python, I experience {}.".format(", ".join(cls().feelings)))
#
#
# def i_love_python():
#     """
#     LovePython Class
#
# This class represents a declaration of love for the Python programming language. It encapsulates reasons why the author loves Python and expresses their feelings towards it.
#
# Attributes:
# - feelings (list): A list of strings representing the feelings experienced when working with Python.
# - reasons (list): A list of strings representing the reasons why the author loves Python.
#
# Methods:
# - __init__(self): Constructor method initializes the LovePython object by setting up the feelings and reasons attributes.
# - express_love(self): Method prints out the reasons why the author loves Python and expresses their feelings.
#
# Usage:
# Instantiate an object of the LovePython class and call the express_love() method to see the reasons and feelings behind the author's love for Python.
#
# Example:
#     my_love = LovePython()
#     my_love.express_love()
#
# Output:
#     Why I love Python:
#     - Python is a simple and understandable language that makes programming fascinating.
#     - A large number of libraries and frameworks make Python an ideal choice for various tasks.
#     - Readable Python syntax makes the code understandable and easily maintainable.
#     - Python has an extensive community ready to help and support in any matter.
#     - A multitude of opportunities for automating routine tasks make life easier and more exciting.
#     - The beautiful philosophy of Python, based on clarity and simplicity, aligns with my views on coding.
#     Every time I write code in Python, I experience excitement, inspiration, and amazement.
#
# """
#     return "I love Python!"
#
#
# if __name__ == '__main__':
#     my_love = LovePython()
#     my_love.express_love()  # Added parentheses to call the method
#     assert i_love_python() == "I love Python!"

#
# def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
#     if abs(len(str1) - len(str2)) > threshold:
#         return False
#     differences = sum(1 for char1, char2 in zip(str1, str2) if char1 != char2)
#     return differences <= threshold
#
#
# print("Example:")
# print(fuzzy_string_match("apple", "appel", 2))
# # These "asserts" are used for self-checking
# assert fuzzy_string_match("apple", "appel", 2) == True
# assert fuzzy_string_match("apple", "bpple", 1) == True
# assert fuzzy_string_match("apple", "bpple", 0) == False
# assert fuzzy_string_match("apple", "apples", 1) == True
# assert fuzzy_string_match("apple", "bpples", 2) == True
# assert fuzzy_string_match("apple", "apxle", 1) == True
# assert fuzzy_string_match("apple", "pxxli", 3) == False
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def to_camel_case(name: str) -> str:
#     name = name.replace('_', ' ')
#     return ''.join(word.capitalize() for word in name.split())
#
#
# print("Example:")
# print(to_camel_case("my_function_name"))
# # These "asserts" are used for self-checking
# assert to_camel_case("my_function_name") == "MyFunctionName"
# assert to_camel_case("i_phone") == "IPhone"
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def caps_lock(text: str) -> str:
#     caps_lock_on = False
#     result = ""
#     for char in text:
#         if char == 'a':
#             caps_lock_on = not caps_lock_on
#         elif caps_lock_on and 'a' <= char <= 'z':
#             result += char.upper()
#         else:
#             result += char
#     return result
#
#
# print("Example:")
# print(caps_lock("Why are you asking me that?"))
# # These "asserts" are used for self-checking
# assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
# assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
# assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
# print("The mission is done! Click 'Check Solution' to earn rewards!")
