#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint


def enter_user_num(text):
    digit = 0
    while (digit == 0):
        digit = int(input(text))
    return digit

def autocomplete_list(n):
    list = []
    for i in range (n):
        list.append(randint(-n,n))
    return list

def product_list(list, n):
    prod_list = []
    for j in range(len(list)):
        while j < len(list)/2 and n > len(list)/2:
            n -= 1
            a = list[j] * list[n]
            prod_list.append(a)
            j += 1
    return prod_list

users_digit = enter_user_num("введите размер массива: ")
first_list = autocomplete_list(users_digit)
second_list = product_list(first_list, users_digit)
print(first_list)
print(second_list)