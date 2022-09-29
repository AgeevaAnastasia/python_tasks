# напишите программу, где пользователь введет 2 строки, а программа проверит, сколько вхождение одной строки в другую

first_str = input('Введите первую строку: ')
second_str = input('Введите вторую строку: ')
if len(first_str) > len(second_str):
    cnt = first_str.count(second_str)
    if cnt == 0:
        print('нет вхождений одной строки в другую')
    else:
        print(f'Количество вхождение второй строки в первую: {cnt}')
else:
    cnt = second_str.count(first_str)
    if cnt == 0:
        print('нет вхождений одной строки в другую')
    else:
        print(f'Количество вхождение первой строки во вторую: {cnt}')
