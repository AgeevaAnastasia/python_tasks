# Проверить истинность утверждения не (X или Y или Z) = не X и не Y и не Z


def logical(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    return left == right

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'x {x}, y {y}, z {z}')
            print(logical(x, y, z))
