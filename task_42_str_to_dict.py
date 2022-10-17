# Дана строка:
# 'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'
# Необходимо получить словарь, в котором ключи – слова, значения – количество слов в
# строке:
# {'дом': 2, 'окно': 2, 'дверь': 2, 'стена': 1, 'кухня': 1, 'стол': 2, 'стул': 3}


import re 
from pprint import pprint

print()
my_str = 'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'

marks = '''!()-[];?@#$%:'"\,./^&amp;*_'''
 
for x in my_str:  
    if x in marks:  
        new_str = my_str.replace(x, "")

new_str = new_str.split(' ')

my_dict = {}

for item in new_str:
    my_dict.setdefault(item, 0)


for item in new_str:
    for key in my_dict:
        if item == key:
            temp = my_dict[key] + 1
            my_dict[key] = temp
            

pprint(my_dict)
print()
