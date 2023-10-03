
# Вывод информации 
def printInfo(phoneDerictore):
    print("\nФамилия, Имя, Номер")
    with open(phoneDerictore, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Ввод ФИО и номер
def inputInfo(phoneDerictore):
    with open(phoneDerictore, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(phoneDerictore, "a", encoding="utf-8") as data: 
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"{num}, {fio}, {phone_number}\n")
        print(f"Добавлена запись : {num}, {fio}, {phone_number}\n")

# Редактор 
def editDerictore(phoneDerictore):
    print("\nФамилия, Имя, Номер")
    with open(phoneDerictore, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(phoneDerictore, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))        

# удаление 
def delete(phoneDerictore):
    print("\nФамилия, Имя, Номер")
    with open(phoneDerictore, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(phoneDerictore, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))        

def main():
    my_choice = -1
    file_tel = "phone.csv"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Меню программы:")
        print("1 - Вывести информацию")
        print("2 - Ввести новый контакт")
        print("3 - Изменить ифнормацию")
        print("4 - Удалить")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            printInfo(file_tel)
        elif action == 2:
            inputInfo(file_tel)
        elif action == 3:
            editDerictore(file_tel)
        elif action == 4:
            delete(file_tel)
        else:
            my_choice = 0

main()        