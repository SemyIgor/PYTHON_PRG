from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import controller as con
import user_interface as ui
import logger as log

global active_base


# Section of choices
#
# Контролирует правильность выбора
def getting_main_choice(update: Update, context: CallbackContext):
    chosen = ui.choice_base_convertor(update, context)
    while chosen != '1' and chosen != '2' and chosen != '3' and chosen != '0':
        print('Ошибка! Повторите выбор')
        chosen = ui.choice_base_convertor(update, context)
    return chosen


def getting_convertor_choice():  # Выбор конвертирования
    convrt = ui.convertor_menu()
   #  while chosen != '1' and chosen != '2' and chosen != '3':
    while convrt not in ['1', '2', '3', '4', '5', '6']:
        print('Ошибка! Повторите выбор')
        convrt = ui.convertor_menu()
    return convrt


def getting_base_option_choice():  # Выбор действий с загруженной базой
    base_option = ui.base_option_menu()
    while base_option not in ['1', '2', '3', '4', '5', '6']:
        print('Ошибка! Повторите выбор')
        base_option = ui.base_option_menu()
    return base_option

# Section of the save / load functions


def get_txt_file():
    print('Загружаем txt файл')
    active_base = log.get_txt_data()
    return active_base


def get_csv_file():
    print('Загружаем csv файл')
    active_base = log.get_csv_data()
    return active_base


def get_json_file():
    print('Загружаем json файл')
    active_base = log.get_json_data()
    return active_base


def save_txt_file(active_base):
    print('Сохраняем txt файл')
    log.save_txt_data(active_base)
    return


def save_csv_file(active_base):
    print('Сохраняем csv файл')
    log.save_csv_data(active_base)
    return


def save_json_file(active_base):
    print('Сохраняем json файл')
    log.save_json_data(active_base)
    return

# Section of the base adition functions


def show_base(active_base):
    print('Смотрим базу')
    ui.print_base(active_base)


def add_person(active_base):
    print('Добавить запись в базу')
    active_base.append(ui.base_add_menu())


def remove_person(active_base):
    print('Удалить запись из базы')
    del_person = ui.base_del_menu()
    for person in active_base:
        if person[0] == del_person:
            print(person)
            active_base.remove(person)


def edit_person_fields(active_base):
    print('Редактируем базу')
    edit_person = ui.base_person_edit_menu()
    for person in active_base:
        if person[0] == edit_person:
            new_id = person[0]
            new_surname = input(f'{person[1]} Введите новую фамилию: ')
            new_name = input(f'{person[2]} Введите новое имя: ')
            new_patronymic = input(f'{person[3]} Введите новое отчество: ')
            new_phone = input(f'{person[4]} Введите новый телефон: ')
            active_base.remove(person)
            person = (new_id, new_surname, new_name, new_patronymic, new_phone)
            active_base.append(person)

            # print('Person to edit = {}'.format(person))


def edit_base_structure():
    print('Редактируем структуру базы')


def save_base_changes():
    print('Сохраняем изменения в файл')
