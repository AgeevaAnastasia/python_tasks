# Дано число, проверить, кратно ли оно 5, 10, 15, но не 30

num = int(input('Введите число: '))
if num % 5 == 0 and num % 10 == 0:
    if num % 30 != 0:
        print(f'число {num} кратно 5 и 10, но не кратно 30')
    else:
        print(f'Число {num} не подходит под заданные условия')
elif num % 15 == 0:
    if num % 30 != 0:
        print(f'число {num} кратно 15, но не кратно 30')
    else:
        print(f'Число {num} не подходит под заданные условия')

else:
    print(f'Число {num} не подходит под заданные условия')
print()


# def find(number):
#     if number%30 !=0:
#         if number%5==0 and number%10==0 or number%15==0:
#           return "число кратно"
#     return "число не кратно"
# print(find(num))
