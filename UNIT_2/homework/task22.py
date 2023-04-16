#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

import re

def code(string, shift):
    newStr = [];
    def shiftUpper(char, shift):
        letterValue = ord(char) + int(shift)
        if letterValue > ord('Z'):
            return chr(ord('A') + (letterValue - ord('Z') - 1))
        
        return chr(letterValue)
    
    def shiftLower(char, shift):
        letterValue = ord(char) + int(shift)
        if letterValue > ord('z'):
            return chr(ord('a') + (letterValue - ord('z') - 1))
        
        return chr(letterValue)
    
    for i in string:
        if(i.isalpha()):
            if i.islower():
                newStr.append(shiftLower(i, shift))
            
            if i.isupper():
                newStr.append(shiftUpper(i, shift))

    return "".join(newStr)
    
str = input("Введите строку: ")
shift = input("Введите смещение: ")

print(code(str, shift))