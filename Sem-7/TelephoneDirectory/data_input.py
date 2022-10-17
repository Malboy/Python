def user_name():
    us_name = str(input("Введите имя: "))
    return us_name

def user_surname():
    us_surname = str(input("Введите фамилию: "))
    return us_surname

def user_phone_number():
    phone_num = str(input('введите номер телефона: '))
    # while not(phone_num.isdigit()):
    #     phone_num = str(input())
    return phone_num

def user_description():
    descrip = str(input('введите описание: '))
    return descrip
