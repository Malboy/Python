import data_input as di
import csv_logger as log

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