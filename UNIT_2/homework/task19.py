#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.

str = input("Введите выражение: ").split(" ")
match (str[1]):
    case "+" : print(int(str[0]) + int(str[2]))
    case "-" : print(int(str[0]) - int(str[2]))
    case "//" : print(float(str[0]) // float(str[2]))
    case "/" : print(float(str[0]) / float(str[2]))
    case "%" : print(float(str[0]) % float(str[2]))
    case "*" : print(int(str[0]) * int(str[2]))
