

def add_new_column(data):
    column_name = input("Введите название новой колонки: ")
    for x in data:
        x[column_name] = '*'
    return data