# Создайте список из N элементов от -N до N. Найти произведение элементов на указанных позициях.
# Позиции хранятся в списке positions, создайте его. 

n = int(input('Введите натуральное число: '))
if n < 0:
    n = n * -1
positions = [1,3,4]
list = []
for i in range(-n, n + 1):
    list.append(i)
if len(list) < 5:
    print('недостаточно членов в последовательности')
else:
    print(list[positions[0]] * list[positions[1]] * list[positions[2]])
