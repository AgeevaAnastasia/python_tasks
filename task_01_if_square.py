# ввести 2 числа и проверить, является ли одно квадратом второго

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print()
if a == b ** 2:
    print(f'Число {a} является квадратом числа {b}')
elif b == a ** 2:
    print(f'Число {b} является квадратом числа {a}')
else: print('Ни одно число не является квадратом второго')
print()
