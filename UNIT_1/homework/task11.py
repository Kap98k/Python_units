#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

lst =  [1, 2, 5, 6, 8, 10, 12]
i = 0;

while i < len(lst):
    lst[i] = lst[i] + 1
    i+=1;

print(lst)

for i in range(len(lst)):
    lst[i] += 1

print(lst)