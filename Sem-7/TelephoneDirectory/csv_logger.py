from datetime import datetime as dt

def create_csv_file():
    try :
        open("manual.csv")
    except IOError as e:
        with open("manual.csv", 'a') as file:
            file.write('date;time;name;surname;telephone number;comment\n')

def add_new_user(nam_d, s_d, num_d, d_d):
    time = dt.now().strftime("%y-%m-%d; %H:%M:%S")
    with open("manual.csv", 'a') as file:
        file.write('{};{};{};{};{}\n'.format(time, nam_d, s_d, num_d, d_d))