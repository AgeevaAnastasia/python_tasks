# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк какое-либо число 

def input_string():
    list_string = input('Введите список строк через пробел: ')
    list_string = list_string.split(' ')
    return list_string

def find_number_in_list(list_string):
    for item in list_string:
        elem = item
        if not (item.find(',') > -1 and elem.find('.') > -1):   # если нет сразу и . и , в строке одновременно
            if item.find(',') > -1:                             # если есть , убираем её
                elem = item.replace(',', '', 1)
            if elem.find('.') > -1:                             # если есть . убираем её
                elem = elem.replace('.', '', 1)
        if elem.find('-') > -1:                                  # если есть - убираем её
            elem = elem.replace('-', '', 1)
        if elem.isdigit():                                       # если остались только цифры, то есть число
            print(f'в вашем списке есть число {item}')
    return

list_string = input_string()
print(f'Список строк {list_string}')
find_number_in_list(list_string)