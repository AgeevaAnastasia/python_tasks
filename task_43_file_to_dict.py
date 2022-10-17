# Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# по аналогии с предыдущим заданием составить аналогичный словарь.

import re 
from pprint import pprint
my_str = ''
print()
path = 'jack.txt'
data = open(path, 'r', encoding='cp1251')
for line in data:
    a = data.readline()
    my_str += a
data.close() 

my_str = my_str.lower()
my_str = my_str.replace('\n', ' ')
my_str = my_str.replace(',', '')


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
