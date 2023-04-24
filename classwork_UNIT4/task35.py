#todo: Заданы два списка. Необходимо их сериализовать в один файл.

import json

list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]

with open("task35.json", "w") as file:
    json.dump(list_one + list_two, file)