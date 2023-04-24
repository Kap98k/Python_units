#todo:
# Реализовать декоратор который подсчитывает время выполнения функции.

import time


def executionTime(func):
    def wrapper(lst: list):
        startTime = time.time()
        ret = func(lst)
        print(f"#{time.time() - startTime} seconds#")

        return ret
    
    return wrapper

@executionTime
def listSumm(lst: list) -> int:
    return sum(lst)

print(listSumm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 124, 234, 345, 546, 1, 23, 23, 645]))