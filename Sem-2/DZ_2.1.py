def UserNum(text):
    num = 0
    while (num == 0):
        num = float(input(text))
    return num


def FindSumofNmbers(digit):
    if float(digit) < 0:
        digit = float(digit) * -1
    sum = 0
    for i in str(digit):
        if i != '.':
            sum += int(i)
    return sum


userNumber = UserNum("введите число: ")
result = round(FindSumofNmbers(userNumber))
print(result)
