import random


def write_file(equation):
    with open('final_file.txt', 'w') as data:
        data.write(equation)


def create_mn(k):
    my_list = [random.randint(0,101) for i in range(k+1)]
    return my_list
    

def create_equation(sp):
    my_list = sp[::-1]
    part = ''
    if len(my_list) < 1:
        part = 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                part += f'{my_list[i]}x^{len(my_list)-i-1}'
                if my_list[i+1] != 0:
                    part += ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                part += f'{my_list[i]}x'
                if my_list[i+1] != 0:
                    part += ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                part += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                part += ' = 0'
    return part

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_equation(koef))