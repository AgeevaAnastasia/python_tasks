# Вывести на экран числа от -N  до N

# Применила list comprehension




num = int(input('Введите целое число: '))


def print_nums(number):
    number = abs(number) # если введено отрицательное число, сделает его положительным
    first = number * -1
    second = number
    my_list = [i for i in range(first, second + 1)]
    print(*my_list)

        
print_nums(num)
