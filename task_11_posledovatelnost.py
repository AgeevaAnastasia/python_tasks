# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
# N = 5: 1, -3, 9 -27, 81

n = int(input('Введите число N: '))
print(f'N = {n}: ', end = '')
sign = 1
for i in range(0, n - 1):
    print(f'{3 ** i * sign}, ', end = '')
    sign = -sign
print(f'{3 ** (n - 1) * sign}', end = '')
