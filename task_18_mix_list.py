# Реализовать алгоритм перемешивания списка

list = list(input('Введите элементы списка через пробел:').split(' '))
print(list)
for i in range(len(list)):
    for j in range(len(list) - i):
        x = list[i]
        list[i] = list[j]
        list[j] = x
    
print(list)

