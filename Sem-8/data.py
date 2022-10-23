from imghdr import what
import json_data as jd
import menu as m
import new_column as nc
import new_string as ns
import edit_string as es
import data_base_show as dbs
import os


def data_com():
    file = os.path.isfile("data_file.json")
    if file == False:
        data = []
        jd.write_in_file(data)
    data = jd.read_file()
    exit = True
    while (exit):
        action = m.menu()
        if action == '1':
            dbs.show_db(data)
        elif action == '2':
            nc.add_new_column(data)
        elif action == '3':
            ns.add_new_string(data)
        elif action == '4':
            es.change_data_in_str(data)
        elif action == '5':
            jd.write_in_file(data)
        elif action == '0':
            exit = False
        else:
            print("не вверно введена команда")
            
