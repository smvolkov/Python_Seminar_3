# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите десятичное число: '))
binar = []

while n > 0:
    binar.append(n % 2)
    n = int(n / 2)
    
j = len(binar)

while j > 0:
    print (binar[j-1], end ="")
    j -= 1

