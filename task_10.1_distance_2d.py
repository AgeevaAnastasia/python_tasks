# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве.

# Применила lambda

print()
print('Введите координаты точки А: ')
ax = int(input('x = '))
ay = int(input('y = '))
print('Введите координаты точки B: ')
bx = int(input('x = '))
by = int(input('y = '))
print()

res = (lambda a, b, c, d: round(((c - a)**2 + (d - b)**2) ** 0.5, 2))(ax, ay, bx, by)
print(f'A ({ax}, {ay}); B ({bx}, {by})  ->  {res}')
