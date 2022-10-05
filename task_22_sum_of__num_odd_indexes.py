# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

l = [int(x) for x in input('Введите числа в список через запятую: ').split(',')]
sum = 0
for i in range(len(l) - 1):
    if i % 2 == 1:
        sum += l[i]

print(l, end = ' ')
print(f'-> {sum}')