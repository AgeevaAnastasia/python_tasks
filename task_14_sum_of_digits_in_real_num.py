# Подсчитать сумму цифр в вещественном числе

num = input('Введите вещественное число: ')
num = num.replace('.', '')
num = num.replace(',', '')
res = 0
for i in num:
    res = res + int(i)
print(res)
