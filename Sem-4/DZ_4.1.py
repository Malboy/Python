from math import *

def enter_user_num(text):
    num = str(input(text))
    while (not(num.isdigit())):
        num = str(input(text))
    return int(num)


d = enter_user_num("Введите кол-во знаков после запятой у числа pi: ")
print(f'число Пи с  точностью до {d} знаков после запятой равно {round(pi, d)}')
