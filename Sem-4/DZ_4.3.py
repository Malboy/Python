
def create_first_list():
    my_list = list(map(int, input("Введите числа через пробел:\n").split()))
    return my_list

def find_uncopyed_digits(my_list):
    dublicate_list = []
    [dublicate_list.append(i) for i in my_list if i not in dublicate_list]
    return dublicate_list

list_1 = create_first_list()
print(f"Исходный список: {list_1}")
list_2 = find_uncopyed_digits(list_1)
print(f"Список из неповторяющихся элементов: {list_2}")