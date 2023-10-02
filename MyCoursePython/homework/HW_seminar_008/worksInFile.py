from csv import DictReader
from csv import DictWriter
from os.path import exists

def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()

def get_info():
    row_number = input('Введите номер строки для редактирования: ')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return [row_number, last_name, first_name, phone_number]

def write_file(lst):
    with open('phone.csv', 'r+', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        row_number = int(lst[0])
        obj = {'Фамилия': lst[1], 'Имя': lst[2], 'Номер': lst[3]}
        res[row_number] = obj
        data.seek(0)
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writerows(res)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                create_file()
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
            action = input('Введите действие (a - добавить, e - редактировать): ')
            if action == 'a':
                write_file(get_info())
            elif action == 'e':
                write_file(get_info())

main()