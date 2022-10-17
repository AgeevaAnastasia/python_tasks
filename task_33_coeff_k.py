# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
print()

coef = []
for i in range(3):
    coef.append(randint(0, 101))

k = int(input('Задайте степень k > 0: '))


def print_to_file(coef, k):
    str_output = "" 
    if coef[0] != 0:
        if coef[0] != 1: str_output += str(coef[0])
        str_output += 'x'
        if k > 1:
            str_output += '^'
            str_output += str(k)
        str_output += ' + '
        
    if coef[1] != 0:
        if coef[1] != 1: str_output += str(coef[1])
        if k > 1: str_output += 'x'
        if k > 2: 
            str_output += '^'
            str_output += str(k - 1)
        if coef[2] != 0: str_output += ' + '

    if coef[2] != 0:
        if coef[2] != 1 and k <= 3: str_output += str(coef[2])
        elif k <= 2 and coef[2] != 0: str_output += str(coef[2])
        if k > 2: str_output += 'x'
        if k > 3: 
            str_output += '^'
            str_output += str(k - 2)
        
    str_output += ' = 0'
    if coef[0] == 0 and coef[1] == 0: str_output = 'Многочлен не существует'
    return str_output       

res = print_to_file(coef, k)

with open('file.txt', 'w') as f:
    f.write(res)
f.close()
