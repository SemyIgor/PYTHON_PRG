import user_interface as ui
import model as mod
import logger as log
import pprint


def run():
    todo = mod.todo_choice()  # Получили корректный выбор
    if todo == '1':  # импортируем в память из txt файла
        txt_data = log.get_txt_data()
        ui.show_txt_data(txt_data)  # Печать справочника
    elif todo == '2':  # Импортируем в память из csv
        txt_data = log.get_csv_data()
        ui.show_txt_data(txt_data)
    elif todo == '3':  # Импортируем в память из json
        txt_data = log.get_json_data()
        pprint.pprint(txt_data)
    elif todo == '4':  # Экспортируем из выбираемого текстового файла
        frmat = mod.frmat_choice()
        if frmat == '1':  # Из текстового файла в другой txt файл
            txt_data = log.get_txt_data()
            log.book_txt_convertor(txt_data)
        elif frmat == '2':  # Из текстового файла в файл csv
            txt_data = log.get_txt_data()
            log.book_csv_convertor(txt_data)
        elif frmat == '3':  # Из текстового файла в файл json
            txt_data = log.get_txt_data()
            log.book_json_convertor(txt_data)
            pprint.pprint(txt_data)

    return
