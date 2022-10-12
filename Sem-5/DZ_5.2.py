from random import randint

def get_candy(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def info_print(name, k, counter, value):
    print(f"Игрок {name} взял {k} конфет, теперь у него {counter}. На столе осталось {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
candys = 2021
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while candys > 28:
    if flag:
        k = get_candy(player1)
        counter1 += k
        candys -= k
        flag = False
        info_print(player1, k, counter1, candys)
    else:
        k = get_candy(player2)
        counter2 += k
        candys -= k
        flag = True
        info_print(player2, k, counter2, candys)

if flag:
    print(f"Победил игрок {player1}")
else:
    print(f"Победил игрок {player2}")