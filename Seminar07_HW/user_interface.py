import logger as log


def todo_choice_input():  # Получаем выбор действий от пользователя
    print('\
1 - Импортировать справочник из текстового документа\n\
2 - Импортировать справочник из формата json\n\
3 - Экспортировать справочник в файл')
    return input()


def get_file_name():
    file_name = input('Введите имя текстового файла (ph2 или ph3):\n')
    return f'Seminar07_HW\{file_name}.txt'


def show_txt_data(txt_data):
    for i in range(len(txt_data)):
        print(i, end=' ')
        for j in range(4):
            print(txt_data[i][j], end=' ')
        print('\r')


def choose_export_format():
    print('\
1 - Экспорт в файл ph1.txt\n\
2 - Экспорт в файл ph1.csv\n\
3 - Экспорт в файл ph1.json')
    return input()
