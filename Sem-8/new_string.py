

def add_new_string(data):
    if not data:
        user = {}
        user['Имя'] = input("Введите имя: ")
    else:
        u = data[0]
        user = {}
        for i in u:
            user[i] = input(f"Введите {i}: ")
    data.append(user)
    return data