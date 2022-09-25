def UserNumbers(n):
    a = []
    for i in range(n):
        a.append(input(f"Введите значение {i+1}: "))
    return a


def CheckStatement(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = UserNumbers(3)

if CheckStatement(statement) == True:
    print(f"Истинно")
else:
    print(f"Ложь")