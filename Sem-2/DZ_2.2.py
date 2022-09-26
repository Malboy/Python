from pickle import APPEND


def UserNum(text):
    num = 0
    while (num == 0):
        num = int(input(text))
    return num


def CreateList(num):
    prod = 1
    product_list = list()
    for i in range(1, num + 1):
        prod *= i
        product_list.append(prod)
    print(product_list)


digit = UserNum('Введите число: ')
CreateList(digit)
