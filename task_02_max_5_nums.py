a = [5,66,33,54,88]

def find_max_value(list):
    index = 0
    max = list[0]
    max_index = len(list) - 1
    while index <= max_index:
        if list[index] > max:
            max = list[index]
        index += 1
    return max

print(find_max_value(a))
