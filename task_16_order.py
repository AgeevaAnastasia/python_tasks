# Задать список из n чисел последовательности (1 + 1 / n) в степени n. И вывести на экран их сумму

n = int(input('Введите натуральное число: '))
res = 0
list = []
for i in range(1, n + 1):
    list.append((1 + 1 / i) ** i)
    res = res + (1 + 1 / i) ** i
print(list)
print(res)
