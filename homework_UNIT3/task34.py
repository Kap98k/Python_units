# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def sumn(n: int):
    if n > 0:
        x = n + sumn(n-1)
        print(x)
        return x

sumn(10)