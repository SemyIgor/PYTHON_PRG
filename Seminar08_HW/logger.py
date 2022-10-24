import csv
import json
import user_interface as ui
import controller as con


# Read data from the files module
def get_txt_data():
    with open(ui.get_file_name()+'.txt', 'r', encoding='utf-8-sig') as file:
        txt_book = []
        # fields_number = file.readline().rstrip()
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
    with open(ui.get_file_name()+'.csv', encoding='utf-8-sig') as c_file:
        txt_book = []
        while True:  # Считываем по одному абоненту
            txt_book_script = tuple(c_file.readline().rstrip().split(';'))
            if txt_book_script[0] == '':
                break
            txt_book.append(txt_book_script)
    return txt_book


def get_json_data():
    with open(ui.get_file_name()+'.json', 'r', encoding='utf-8-sig') as file:
        txt_book = json.load(file)
    return txt_book

# Save data to the files module


def save_txt_data(active_base):
    with open(ui.get_file_name()+'.txt', 'w') as file:
        for i in active_base:
            file.write(
                f'{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n')
            # f'{i[0]}; {i[1]}; {i[2]}; {i[3]}\n')
    return


def save_csv_data(active_base):
    with open(ui.get_file_name()+'.csv', 'w') as file:
        for i in active_base:
            file.write(
                f'{i[0]}; {i[1]}; {i[2]}; {i[3]}\n')
            # f'{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n')
    return


def save_json_data(active_base):
    with open(ui.get_file_name()+'.json', 'w', encoding='utf-8-sig') as file:
        json.dump(active_base, file, ensure_ascii=False)
    return
