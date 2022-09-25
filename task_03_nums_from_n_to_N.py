# Вывести на экран числа от -N  до N

num = int(input('Введите целое число: '))

def print_nums(number):
    number = abs(number) # если введено отрицательное число, сделает его положительным
    first = number * -1
    second = number
    for i in range(first, second + 1):
        print(i, end = ' ')
    print()

        
print_nums(num)
