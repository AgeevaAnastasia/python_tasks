# Задать список из n чисел последовательности (1 + 1 / n) в степени n. И вывести на экран их сумму

n = int(input('Введите натуральное число: '))


def list_numbers(num):
    res = []
    for i in range(1, num + 1):
        form = (1 + 1 / i) ** i
        res.append(form)
    return(res)

print(list_numbers(n))
print(sum(list_numbers(n)))
