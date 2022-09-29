from random import randrange

with open("file.txt", "w+") as my_file:
    my_file.write("1\n")
    my_file.write("5\n")
    my_file.write("7\n")

def UserNum(text):
    num = 0
    while (num == 0):
        num = int(input(text))
    return num

def CreateRandomList(n):
    randomlist = []
    for i in range(0, n):
        randomlist.append(randrange(-n, n))
    return randomlist    

def GetDigitsFromFile(importfile):
    data = open(importfile, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def FindResult(rand_list, file_list):
    result = 1
    for i in file_list:
        result *= rand_list[i]
    return result


file = 'file.txt'
N = UserNum('Введите число: ')
list = CreateRandomList(N)
impList = GetDigitsFromFile(file)
print(list)
print(impList)
print(FindResult(list,impList))