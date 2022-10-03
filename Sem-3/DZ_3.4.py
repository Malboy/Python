#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def enter_user_num(text):
    digit = 0
    while (digit == 0):
        digit = int(input(text))
    return digit

def turn_to_double(n):
    dig = ""
    while n != 0:
        dig = str(n%2) + dig
        n //=2
    return dig

digit = enter_user_num("введите число: ")
digit_1 = turn_to_double(digit)

print(f"Это же число в двоичной системе счисления: {digit_1}")
