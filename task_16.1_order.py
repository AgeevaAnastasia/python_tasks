# Задать список из n чисел последовательности (1 + 1 / n) в степени n. И вывести на экран их сумму

n = int(input('Введите натуральное число: '))

res = list(map((lambda x: (1 + 1 / x) ** x), [i for i in range(1, n + 1)]))

print(res)
print(sum(res))
