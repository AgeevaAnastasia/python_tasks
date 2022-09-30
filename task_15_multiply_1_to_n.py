# Напишите программу, получающую набор произведение от 0 до n

n = int(input('Введите число N: '))

def multiply(num):
    mult = 1
    l = []
    for i in  range(1, num + 1):
        mult *= i
        l.append(mult)
    return(l)

print(f'N = {n}: {multiply(n)}')
