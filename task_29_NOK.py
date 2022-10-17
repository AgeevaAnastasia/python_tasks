# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

for i in range(1, 100000000):
    if i % a == 0 and i % b == 0:
        print(f'Наименьшее общее кратное чисел {a} и {b} равно {i}')
        break



# решение Марата

def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def nok(a, b):
    return int(abs(a * b) / nod(a, b))

print(nok(a, b))
print(nod(a, b))
