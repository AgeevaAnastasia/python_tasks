# Подсчитать сумму цифр в вещественном числе

num = input('Введите вещественное число: ')
def sum_num(number):
    res = 0
    for i in number:
        if i == '.' or i == ',': 
            continue
        res += int(i)
    return(res)

print(f'сумма числе в числе {num} равна {sum_num(num)}')



# Более медленный вариант:
# num = num.replace('.', '')
# num = num.replace(',', '')
# res = 0
# for i in num:
#     res = res + int(i)
# print(res)
