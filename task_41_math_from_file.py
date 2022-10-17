# 1.Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;


data = open('math.txt', 'r')
my_str = data.readline()
data.close()


def get_list(my_str):
    my_str = list(my_str)
    a = ''
    new_list = []
    for i in my_str:
        if i.isdigit():
            a += i
        else:
            if a != '':
                new_list.append(int(a))
                a = ''
            new_list.append(i)
    if a != '':
        new_list.append(int(a))
    return new_list

my_list = get_list(my_str) 
print(my_list)


def score(my_list):
    ss = ''
    def action(ss, l):
        for i in range(l):
            if my_list[i] == ss:
                if ss == '*':
                    a = my_list[i - 1] * my_list[i + 1]
                elif ss == '/':
                    a = my_list[i - 1] / my_list[i + 1]
                elif ss == '+':
                    a = my_list[i - 1] + my_list[i + 1]
                elif ss == '-':
                    a = my_list[i - 1] - my_list[i + 1]
                my_list[i] = a
                my_list.pop(i - 1)
                my_list.pop(i)
                print(my_list)
                l -= 2
                break
            
            
        return my_list
            
    
    l = len(my_list)   
    while '*' in my_list:
        my_list = action('*', l)
    print(my_list)
        
    while '/' in my_list:
        my_list = action('/', l) 
    print(my_list) 
        
    while '+' in my_list:
        my_list = action('+', l)
    print(my_list)
        
    while '-' in my_list:
        my_list = action('-', l)  
    print(my_list)
        
        
    return my_list
            


res = score(my_list)
print(my_str, end = ' => ')             

print(*res)




