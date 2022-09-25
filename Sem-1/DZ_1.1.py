def switch_case(day):
    if day == 1:
        return print(day," - нет")
    elif day == 2:
        return print(day, " - нет")
    elif day == 3:
        return print(day," - нет")
    elif day == 4:
        return print(day," - нет")
    elif day == 5:
        return print(day," - нет")
    elif day == 6:
        return print(day," - да")
    elif day == 7:
        return print(day," - да")
    else:
        return print("Введено не правильное число")



day = int(input("Введите число от 1 до 7: "))
switch_case(day)