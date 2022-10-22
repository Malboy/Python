from imghdr import what
import json_data as jd
import menu as m
import new_column as nc
import new_string as ns
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
            show_db()
        if action == '2':
            nc.add_new_column(data)
        if action == '3':
            ns.add_new_string(data)
        if action == '4':
            change_data_in_str()
        if action == '5':
            jd.write_in_file(data)
        else:
            exit = False
            
