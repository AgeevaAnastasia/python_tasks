# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк заданное число



print()


def input_string():
    list_string = input('Введите список строк через пробел: ')
    list_string = list_string.split(' ')
    return list_string


def find_number_in_list(list_string, number):
    for item in list_string:
        if number in item:
            print(f'В элементе списка {item} есть число {number}')


list_string = input_string()
num = input("Введите число: ")
print(f'Список строк {list_string}')
find_number_in_list(list_string, num)
print()
print()
