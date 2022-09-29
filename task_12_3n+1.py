# Для натурального N создать последовательность 3n+1 (n = 6: [4, 7, 10, 13, 16, 19])

n = int(input('Введите число N: '))
print(f'n = {n}: ', end = '')
# for i in range(1, n):
#     print(f'{3 * i + 1}, ', end = '')
# print(f'{3 * n + 1}]')

result = []
for i in range(1, n + 1):
    result.append(3 * i + 1)
print(*result, sep=', ')
