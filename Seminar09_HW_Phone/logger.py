# import csv


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_csv_data():
    with open('base.csv', encoding='utf-8-sig') as c_file:
        txt_book = []
        while True:  # Считываем по одному абоненту
            txt_book_script = tuple(c_file.readline().rstrip().split(';'))
            if txt_book_script[0] == '':  # Если считана пустая строка,
                break  # то выходим из функции считывания
            txt_book.append(txt_book_script)  # Добавляем кортеж в строку
    return txt_book  # Возвращаем список кортежей
# --------------------------------------------------------------------------
