import xml_creator as xc
import csv_logger as cl
import data_input as di


print('Добро пожаловать в Главное меню:\n')
print('Вам доступны следующие команды:\n')
print('Нажмите 1 - сделать новую запись')
print('Нажмите 2 - сформировать xml-файл')
print('Нажмите 0 - выйти из программы')

def get_user_num():
    num = str(input("введите номер команды: "))
    while (not(num.isdigit()) or num not in ['0','1','2']):
        num = str(input('Введён не корректный номер. Повторите ввод: '))
    return num

def command_wait(user_dig):
    match user_dig:
        case "1":
            # cl.name_log(di.user_name())
            # cl.surname_log(di.user_surname())
            # cl.phone_number_log(di.user_phone_number())
            # cl.description_log(di.user_description())
            cl.add_new_user(di.user_name(), di.user_surname(), di.user_phone_number(), di.user_description())
        case "2":
            xc.create()
        case "0":
            exit()

dig = get_user_num()
command_wait(dig)