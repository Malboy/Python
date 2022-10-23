

def add_new_column(data):
    column_name = input("Введите название нового ключа: ")
    for x in data:
        x[column_name] = '*'
    return data