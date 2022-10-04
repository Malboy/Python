def enter_user_num(text):
    num = str(input(text))
    while (not(num.isdigit())):
        num = str(input(text))
    return int(num)

def simp_of_num(nomer, i):
    list = []
    while i <= nomer:
        if nomer % i == 0:
            list.append(i)
            nomer //= i
            i = 2
        else:
            i += 1
    return list

N = enter_user_num("Введите натуральное число: ")
simp_num = 2
simp_list = simp_of_num(N, simp_num)
print(f"Простые множители числа {N} приведены в списке: {simp_list}")