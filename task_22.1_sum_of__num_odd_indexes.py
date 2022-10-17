# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Применила list comprehension

l = [int(x) for x in input('Введите числа в список через запятую: ').split(',')]

l_odd = [l[i] for i in range(len(l)) if i % 2 != 0]
print(l_odd)

s = sum(l_odd)

print(l, end = ' ')
print(f'-> {s}')
