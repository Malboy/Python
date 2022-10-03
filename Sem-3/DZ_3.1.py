#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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

def find_odd_sum(list):
    odd_sum = 0
    for index in range(len(list)):
        if index % 2 == 1:
            odd_sum += list[index]
    return odd_sum


users_digit = enter_user_num("введите размер массива: ")
complete_list = autocomplete_list(users_digit)
odd_sum_in_list = find_odd_sum(complete_list)
print(len(complete_list))
print(complete_list)
print(odd_sum_in_list)