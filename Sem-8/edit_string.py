import json

def change_data_in_str(data):
    s = int(input("Введите номер пользователя, данные которого выхотите изменить: "))
    if not data[s]:
        print("Такого нет")
    else:
        column_name = input("Введите название ключа, которое вы хотите изменить: ")
        data[s][f"{column_name}"] = input(f"Введите новое значение {column_name}: ")
    return data