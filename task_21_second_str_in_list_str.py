# Напишите программу, которая определит второе вхождение строки в листе строк. Или вернет ошибку, если его нет

print()


def input_string():
    list_string = input('Введите список строк через пробел: ')
    list_string = list_string.split(' ')
    return list_string


list_string = input_string()
string_find = input("Введите строку для поиска в списке: ")
print(f'Список строк {list_string}')

if list_string.count(string_find) > 1:
    position = list_string.index(string_find)    # позиция первого вхождения
    position = list_string.index(string_find, position + 1)   # позиция второго вхождения
    print(f'Позиция второго вхождения - {position}')
else: print('Нет второго вхождения')

print()
print()
