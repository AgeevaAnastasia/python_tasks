# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

l = input('Введите числа через пробел: ').split(' ')


def find_max(nums):
    max_num = nums[0]
    for i in nums:
        if i > max_num:
            max_num = i
    return max_num


def find_min(nums):
    min_num = nums[0]
    for i in nums:
        if i < min_num:
            min_num = i
    return min_num


max_number = find_max(l)
min_number = find_min(l)

print(f'Максимальное число: {max_number}, минимальное число: {min_number}')