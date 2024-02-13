# import functools
# import time
#
#
# def benchmark(func):
#     """Декоратор, замеряющий время выполнения функции.
#     Далее мы используем его на функции, которая делает GET-запрос к главной странице Google.
#     Чтобы измерить скорость, мы сначала сохраняем время перед выполнением обёрнутой функции,
#     выполняем её, снова сохраняем текущее время и вычитаем из него начальное."""
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#         return return_value
#     return wrapper
#
#
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.status_code, webpage.url
#
#
# webpage = fetch_webpage('https://google.com')
# print(webpage)


# ------------------------------------------------------------

import functools
import time


def time_execution_func(func):
    """Этот декоратор принимает функцию и
     просчитывает время её выполнения"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("Время выполнения функции {} = {}".format(func, time.time() - start_time))
        return result
    return wrapper


@time_execution_func
def power(a, b):
    return a ** b


print(power(2, 18))
