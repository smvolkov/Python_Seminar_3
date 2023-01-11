# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.ДОП

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число k: '))

fibonacci = [0] * (k * 2 + 1)
fibonacci[k] = 0

i = j = k
while j > 0:
    if j == k:
        fibonacci[j - 1] = fibonacci[i + 1] = 1
    else:
        fibonacci[j - 1] = fibonacci[j + 1] - fibonacci [j]
        fibonacci[i + 1] = fibonacci[i] + fibonacci [i - 1]
    i += 1
    j -= 1
    
print(fibonacci)

