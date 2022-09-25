def userNum(text):
    num = 0
    while (num == 0):
        print("Введите число отличное от нуля: ")
        num = float(input(text))
    return num

def CheckQarter(X,Y):
    if (X > 0 and Y > 0):
        print("Первая четверть")
    elif (X < 0 and Y > 0):
        print("Вторая четверть")
    elif (X < 0 and Y < 0):
        print("Третья четверть")
    else:
        print("Четвертая четверть")

x = userNum("Введите значение Х: ")
y = userNum("Введите значение Y: ")

CheckQarter(x, y)