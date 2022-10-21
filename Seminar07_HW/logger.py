import json
import user_interface as ui


def old_book():
    txt_data = [
        ('Григорьев', 'Никита', 'Дмитриевич', '+7(946)0123360'),
        ('Берёзкина', 'Олеся', 'Владимировна', '+7(981)2155632'),
        ('Лапкин', 'Василий', 'Сергеевич', '+7(303)7651902'),
        ('Брюлик', 'Юлия', 'Гавриловна', '+7(673)6377964')
    ]
    return txt_data


def get_txt_data():
    with open(ui.get_file_name(), 'r', encoding='utf-8-sig') as file:
        txt_book = []
        while True:  # Считываем по одному абоненту
            txt_book_script =\
                (file.readline().rstrip(),  # Убираем символ перевода строки
                    file.readline().rstrip(),
                    file.readline().rstrip(),
                    file.readline().rstrip())
            if txt_book_script[0] == '':
                break
            txt_book.append(txt_book_script)
    return txt_book


def get_csv_data():
    with open('Seminar07_HW\ph1.csv', 'r', encoding='utf-8-sig') as file:
        txt_book = []
        while True:  # Считываем по одному абоненту
            txt_book_script = tuple(file.readline().rstrip().split(';'))
            if txt_book_script[0] == '':
                break
            txt_book.append(txt_book_script)
    return txt_book


def get_json_data():
    with open('Seminar07_HW\ph1.json', 'r', encoding='utf-8-sig') as file:
        txt_book = json.load(file)
    return txt_book


def book_csv_convertor(txt_data):
    with open('Seminar07_HW\ph1.csv', 'w') as file:
        for i in txt_data:
            file.write(
                f'{i[0]}; {i[1]}; {i[2]}; {i[3]}\n')


def book_txt_convertor(txt_data):
    with open('Seminar07_HW\ph1.txt', 'w') as file:
        for i in txt_data:
            file.write(
                f'{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n')


def book_json_convertor(txt_data):
    with open('Seminar07_HW\ph1.json', 'w', encoding='utf-8-sig') as file:
        json.dump(dict(enumerate(txt_data)), file, ensure_ascii=False)
