from math import *


def GetUserNum(text):
    num = 0
    while num == 0:
        print(text)
        num = int(input())
    return num


def FindDistance(x1, y1, x2, y2):
    dist = sqrt(pow(x2-x1, 2)+pow(y2-y1, 2))
    return dist
    #print(f"расстояние между точками {x1},{y1} и {x2},{y2} = {dist}")


x1 = GetUserNum("Введите значение х для точки А: ")
y1 = GetUserNum("Введите значение y для точки А: ")
x2 = GetUserNum("Введите значение х для точки B: ")
y2 = GetUserNum("Введите значение y для точки B: ")

distance = FindDistance(x1, y1, x2, y2)
distance = round(distance, 3)
print (f"расстояние между точками ({x1},{y1}) и ({x2},{y2}) = {distance}")
