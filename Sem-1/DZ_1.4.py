def userNum(text):
    num = 0
    while (num <= 0 or num > 4):
        print(text)
        num = int(input())
    return num

def QuarterCheck(num):
    if (num == 1):
        print("x > 0 и до ∞")
        print("y > 0 и до ∞")
    elif (num == 2):
        print("x < 0 и до -∞")
        print("y > 0 и до ∞")
    elif (num == 3):
        print("x < 0 и до -∞")
        print("y < 0 и до -∞")
    else:
        print("x > 0 и до ∞")
        print("y < 0 и до -∞")

quarter = userNum("Введите число отличное от нуля, в диапазоне от 1 до 4: ")
QuarterCheck(quarter)