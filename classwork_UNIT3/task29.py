#todo:
#  Реализуйте функцию convert(), которая принимает один аргумент:
#  number — целое число
#  Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:
#  двоичное представление числа number в виде строки без префикса 0b
#  восьмеричное представление числа number в виде строки без префикса 0o
#  шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
#  Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().
#  Задачу решить доступным способом
#  Задачу решить с помощью применения функции map и lambda

def slicePrefix(string:str, positive:bool):
    lst = ("0b", "0o", "0x");
    if(x in string for x in lst):
        return string[2:] if positive else string[3:]

def convert(x:int) -> list:
    isPositive = lambda x : x > 0
    return [
        slicePrefix(bin(x), isPositive(x)),
        slicePrefix(oct(x), isPositive(x)),
        slicePrefix(hex(x), isPositive(x))
    ]

def convert_2(x:int) -> list:
    lst = [bin(x), oct(x), hex(x)];
    return list(map(lambda str: slicePrefix(str, x > 0), lst))

print((*convert(64),))

print((*convert_2(81), ))