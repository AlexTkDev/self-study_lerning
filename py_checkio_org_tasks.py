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
import re
import statistics
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