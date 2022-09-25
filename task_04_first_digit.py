# Показать первую цифру дробной части числа

from turtle import clear


num = float(input('Введите число: '))
num_int = int(num)
num = num - num_int
res = int(num * 10)
print(res)
