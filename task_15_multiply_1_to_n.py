# Напишите программу, получающую набор произведение от 0 до n

n = int(input('Введите число N: '))
mult = 1
list = []
for i in  range(1, n + 1):
    mult = i * mult
    list.append(mult)
print(f'N = {n}: {list}')
