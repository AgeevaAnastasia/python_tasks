# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности.

from random import randint
print()

list_input = []
for i in range(20):
    list_input.append(randint(0, 10))
    
list_nonrepetitive = []
cnt = 1

for i in range(len(list_input)):
    for j in range(i + 1, len(list_input)):
        if list_input[i] == list_input[j]:
            cnt += 1
    if cnt == 1:
        list_nonrepetitive.append(list_input[i])
    else: cnt = 1

print(f'Исходный список: {list_input}')
print(f'Список неповторяющихся элементов исходного списка: {list_nonrepetitive}')
