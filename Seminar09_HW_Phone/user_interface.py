from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

global active_base

# Для бота


def choice_base_convertor(update: Update, context: CallbackContext):
    update.message.reply_text('1 - Чтение / Запись файла')
    update.message.reply_text('2 - Работа с базой')
    update.message.reply_text('3 - Просмотр загруженной базы')
    update.message.reply_text('0 - Выход из программы')
    choice = '0'
    # choice = update.message.text
    # choice = update.message.text
    # print(choice)
    # print('1 - Чтение / Запись файла\n'
    #       '2 - Работа с базой\n'
    #       '3 - Просмотр загруженной базы\n'
    #       '0 - Выход из программы')
    # return input()
    return choice

# def choice_base_convertor():
#     print('1 - Чтение / Запись файла\n'
#           '2 - Работа с базой\n'
#           '3 - Просмотр загруженной базы\n'
#           '0 - Выход из программы')
#     return input()


def convertor_menu():
    print('1 - Чтение txt файла\n'
          '2 - Запись txt файла\n'
          '3 - Чтение csv файла\n'
          '4 - Запись csv файла\n'
          '5 - Чтение json файла\n'
          '6 - Запись json файла')
    return input()


def base_option_menu():
    print('1 - Просмотр базы\n'
          '2 - Добавить запись\n'
          '3 - Удалить запись\n'
          '4 - Редактировать поля записи\n'
          '5 - Редактировать структуру базы\n'
          '6 - Сохранить изменения в файл')
    return input()


def base_add_menu():
    new_id = input('Введите новый ID: ')
    new_surname = input('Введите новую фамилию: ')
    new_name = input('Введите новое имя: ')
    new_patronymic = input('Введите новое отчество: ')
    new_phone = input('Введите новый телефон: ')
    return (new_id, new_surname, new_name, new_patronymic, new_phone)


def base_del_menu():
    del_id = input('Введите ID записи к удалению: ')
    return (del_id)


def base_person_edit_menu():
    edit_id = input('Введите ID записи к редактированию: ')
    return (edit_id)


def get_file_name():
    file_name = input('Введите имя файла без расширения:\n')
    return f'Seminar08_HW\{file_name}'


def print_base(active_base):
    for el in active_base:
        print(el)
    print('\n')
    return
