#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint, random


def enter_user_num(text):
    digit = 0
    while (digit == 0):
        digit = int(input(text))
    return digit

def autocomplete_list(n):
    list = []
    for i in range (n):
        list.append(round(randint(0,n) + random(),2))
    return list

def find_difference(list):
    list_of_remainders = []
    for i in range(len(list)):
        if list[i] % 1 != 0:
            list_of_remainders.append(round(list[i] % 1, 2))            
    return round(max(list_of_remainders) - min(list_of_remainders),2)


list_size = enter_user_num("введите размер массива: ")
users_list = autocomplete_list(list_size)
print(users_list)
difference = find_difference(users_list)
print(difference)