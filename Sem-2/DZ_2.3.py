def UserNum(text):
    num = 0
    while (num == 0):
        num = int(input(text))
    return num

def CreateList(n):
    func_list = list()
    for i in range (1, n):
        func_list.append(pow((1 + 1/i), i))
    print(f"итоговый список: {func_list}")
    

N = UserNum('Введите число: ')
CreateList(N)