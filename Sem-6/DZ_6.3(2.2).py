from math import factorial


def UserNum(text):
    num = 0
    while (num == 0):
        num = int(input(text))
    return num


def CreateList(num):
    prod = [i for i in range(1, num+1)]
    prod = list(map(lambda x: factorial(x), prod))
    # prod = 1
    # product_list = list()
    # for i in range(1, num + 1):
    #     prod *= i
    #     product_list.append(prod)
    print(prod)


digit = UserNum('Введите число: ')
CreateList(digit)