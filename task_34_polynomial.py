# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# сделала только простой вариант. Сложные делала, но сильно запуталась. Надеюсь, разберём на семинаре.

data = open('poly1.txt', 'r')
str_poly1 = data.readline()
data.close()


data = open('poly2.txt', 'r')
str_poly2 = data.readline()
data.close()



def str_split(my_str):
    my_str = my_str.replace('x', ' ')
    my_str = my_str.replace('  ', ' ')
    my_str = my_str.split(' ')
    return my_str

str_poly1_list = str_split(str_poly1)
str_poly2_list = str_split(str_poly2)

str_res = []

a = int(str_poly1_list[0]) + int(str_poly2_list[0])
str_res += str(a)
str_res += 'x'
str_res += str_poly1_list[1]
str_res += ' + '
a = int(str_poly1_list[3]) + int(str_poly2_list[3])
str_res += str(a)
str_res += 'x'
str_res += ' + '
a = int(str_poly1_list[5]) + int(str_poly2_list[5])
str_res += str(a)
str_res += ' = 0'
str_res = ''.join(str_res)



data = open('poly_result.txt', 'w')
data.write(str_res)
data.close()
