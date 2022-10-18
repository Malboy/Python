import data_input as di
import csv_logger as log


# def row_view():
#     name_data = di.user_name
#     surname_data = di.user_surname()
#     phone_data = di.user_phone_number()
#     decription_data = di.user_description()
#     log.add_new_user(name_data, surname_data, phone_data, decription_data)
#     return [name_data, surname_data, phone_data, decription_data]

def name_view():
    data = di.user_name()
    log.name_log(data)
    return data

def surname_view():
    data = di.user_surname()
    log.surname_log(data)
    return data

def telephone_num_view():
    data = di.user_phone_number()
    log.phone_number_log(data)
    return data

def descrition_view():
    data = di.user_description()
    log.description_log(data)
    return data