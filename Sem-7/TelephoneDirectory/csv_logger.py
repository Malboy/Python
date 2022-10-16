from datetime import datetime as dt

def name_log(data):
    time = dt.now().strftime("%y-%m-%d; %H:%M:%S")
    with open("manual.csv", 'a') as file:
        file.write('{};name;{}\n'.format(time, data))

def surname_log(data):
    time = dt.now().strftime("%y-%m-%d; %H:%M:%S")
    with open("manual.csv", 'a') as file:
        file.write('{};surname;{}\n'.format(time, data))

def phone_number_log(data):
    time = dt.now().strftime("%y-%m-%d; %H:%M:%S")
    with open("manual.csv", 'a') as file:
        file.write('{};phone_number;{}\n'.format(time, data))

def description_log(data):
    time = dt.now().strftime("%y-%m-%d; %H:%M:%S")
    with open("manual.csv", 'a') as file:
        file.write('{};description;{}\n'.format(time, data))