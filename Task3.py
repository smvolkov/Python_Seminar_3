# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

arr = [1.1, 1.2, 3.1, 5, 10.01]
arr_1 = []

for i in arr:
    arr_1.append(i - int(i))
    
print(max(arr_1) - min(arr_1))