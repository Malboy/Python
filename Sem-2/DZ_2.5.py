from random import randrange

def UserNum(text):
    num = 0
    while (num == 0):
        num = int(input(text))
    return num

def CreateListWithRandomDigits(n):
    list = []
    for i in range (0,n):
        list.append(randrange(-n, n))
    return list

def SwapRandElements(list):
    e1 = randrange(0,len(list))
    e2 = randrange(0,len(list))
    value = 0
    value = list[e1]
    list[e1] = list[e2]
    list[e2] = value

N = UserNum("введите размер массива: ")
my_list = CreateListWithRandomDigits(N)
print(f"Изначальный список: {my_list}")
for i in range (0,5):
    SwapRandElements(my_list)
print(f"Список после перемешивания: {my_list}")
