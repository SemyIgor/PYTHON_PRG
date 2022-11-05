from spy import *
import model as mod
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
from telegram import Bot
from telegram import Update
from secrets import choice
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
# from datetime import datetime


# Константы для меню калькулятора
COUNT, CONT = range(2)  # [0, 1, ...]

# Константы для меню канвертора
SYST, DBIN, DOCT, DHEX, STOP = range(5)  # [0, 1, 3, ...]

# Константы для меню телефонного справочника
MAIN, CHOICE, FIND, SURNAME, STOP = range(5)  # [0, 1, 2, 3, 4, 5, ...]


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет, {update.effective_user.first_name} !')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(
        f'/help - this menu\n/hi - just to greet you\n/time - show time\n/calc - calculates some tasks\n/conv - converts number systems\n/phone - phone base')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    strg = f'{(datetime.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S"))}'
    update.message.reply_text(strg.capitalize())
    # update.message.reply_text(
    #     f'{(datetime.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S"))}')


#   |   message: /calc
#  \/   pointer: entry point
def calc_start(update, context):  # Точка получения ввода от пользователя
    log(update, context)
    update.message.reply_text(
        'Используйте: \n"+" для сложения,\n"-" для вычитания,\n"*" для умножения,\n"/" для деления,\n"**" для возведения в степень\nнапример: 2**3\nВведите пример для вычисления:')
    return COUNT  # Передаёт строку введенного примера


#   |   message: arithmetic string
#  \/   pointer: 1
def calculate(update, context):  # Точка получения ввода от пользователя
    log(update, context)
    msg = update.message.text
    res_ult = msg.strip()  # Обрезаем пробелы по краям строки
    res_ult = eval(res_ult)  # Вычисляем арифметическое выражение
    update.message.reply_text(f'Результат: {res_ult}')  # Выводим результат
    update.message.reply_text(
        'Для продолжения введите: "Да" или "Yes"\nДля выхода введите: /stop')
    return CONT  # Передает решение пользователя "продолжить / выйти"


#   |   message: "Да" или "Yes" или /stop ("продолжить / выйти")
#  \/   pointer: 2
def calc_cont(update, context):  # Точка получения ввода от пользователя
    log(update, context)
    amt = update.message.text
    if amt.strip() == "/stop":  # Если "/stop", а не "Продолжим", например
        return stop(update, context)
    else:
        update.message.reply_text(f'Вы ввели: {amt}\nВведите пример')
    return COUNT  # К началу калькулятора, если не вышли по /stop


def stop(update, context):  # Завершение работы вызванной функции
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


#   |   message: /conv
#  \/   pointer: entry point
def conv_start(update, context):  # Точка входа конвертора
    log(update, context)
    conv_menu(update, context)
    return SYST  # Передаёт строку введенного примера


#   |   message: 1, 2, 3, 4
#  \/   pointer: SYST
def conv_num_sys(update, context):
    num_sys = update.message.text
    print(f'Выбор = {num_sys}')
    if num_sys == '1':
        update.message.reply_text('Введите десятичное число')
        return DBIN
    elif num_sys == '2':
        update.message.reply_text('Введите десятичное число')
        return DOCT
    elif num_sys == '3':
        update.message.reply_text('Введите десятичное число')
        return DHEX
    elif num_sys == '4':
        return stop(update, context)
    else:
        conv_menu(update, context)
        return SYST


def dec_to_bin(update, context):
    dec_num = int(update.message.text)
    print(dec_num)
    update.message.reply_text(
        '{0:d} Соответствует двоичному {0:b}'.format(dec_num, dec_num))
    conv_menu(update, context)
    return SYST


def dec_to_oct(update, context):
    dec_num = int(update.message.text)
    print(dec_num)
    update.message.reply_text(
        '{0:d} Соответствует восьмеричному {0:o}'.format(dec_num, dec_num))
    conv_menu(update, context)
    return SYST


def dec_to_hex(update, context):
    print('Шестнадцать')
    dec_num = int(update.message.text)
    print(dec_num)
    update.message.reply_text(
        '{0:d} Соответствует шестнадцатеричному {0:X}'.format(dec_num, dec_num))

    conv_menu(update, context)
    return SYST


def conv_menu(update, context):
    update.message.reply_text(
        '1 - DEC => BIN\n''2 - DEC => OCT\n''3 - DEC => HEX\n''4 - Выход из программы')
    return


def phone_command(update, context):  # Точка входа телефонного справочника
    log(update, context)
    global active_base  # Доступ к скачиваемому справочнику
    active_base = mod.get_csv_file()  # Загружаем справочник
    update.message.reply_text('Справочник приветствует тебя!')
    update.message.reply_text(
        'Для продолжения введите "y(es)"\n''Для выхода введите "q(uit)"')
    return MAIN


#   |   message: q / y
#  \/   pointer: MAIN
def main_menu(update, context):
    # Выходит из справочника, если получено 'q' или 'quit'
    choice = update.message.text
    # Если решили выйти
    if choice.lower() == 'q' or choice.lower() == 'quit' or choice.lower() == 'й':
        return stop(update, context)
    # Выводит основное меню, если решили продолжить
    elif choice.lower() == 'y' or choice.lower() == 'yes' or choice.lower() == 'н':
        update.message.reply_text('1 - Просмотр справочника')
        update.message.reply_text('2 - Сохранение справочника')
        update.message.reply_text('3 - Редактирование справочника')
        update.message.reply_text('4 - Выход из программы')
        return CHOICE  # К обработке выбранного пункта меню
    else:  # Если решили непонятно что, то возврат в главное меню
        update.message.reply_text(
            'Для продолжения введите "y(es)"\n''Для выхода введите "q(uit)"')
        return MAIN  # В начало главного меню


#   |   message: 1 / 2 / 3 / 4
#  \/   pointer: CHOICE
def main_menu_choice(update, context):
    # Обработка меню справочника
    choice = update.message.text
    if choice == '1':  # Если "Показать справочник"
        show_phones(update, context)  # К функции построчного вывода
        update.message.reply_text(
            'Продолжить - введите y(es), выйти - введите q(uit)')
        return MAIN  # В начало главного меню
    elif choice == '2':  # Если "Сохранение справочника"
        save_phones(update, context)  # К функции сохранения
        update.message.reply_text(
            'Продолжить - введите y(es), выйти - введите q(uit)')
        return MAIN
    elif choice == '3':             # Если "Редактировать справочник",
        edit_book(update, context)  # то к меню редактирования справочника
        return FIND  # К обработке меню редактирования справочника
    elif choice == '4':  # Выход из справочника
        return stop(update, context)
    else:
        # Если введено что-либо, кроме 1, 2, 3, 4
        update.message.reply_text(
            'Продолжить - введите y(es), выйти - введите q(uit)')
        return MAIN


#   |   message: 2
#  \/   pointer: -
def edit_book(update, context):
    update.message.reply_text('1 - Удалить абонента')
    update.message.reply_text('2 - Редактировать абонента')
    update.message.reply_text('3 - Добавить нового абонента')
    update.message.reply_text('4 - Выйти из редактирования справочника')
    # Выводит меню в чат и возвращается в handler за выбором (1, 2, 3, 4)
    return


#   |   message: 1 / 2 / 3 / 4
#  \/   pointer: FIND
def edit_book_choice(update, context):  # Работа со справочником
    global find_choice
    global person_id
    global second_name
    global first_name
    global third_name
    global phone_num
    find_choice = update.message.text
    person_id = ''
    second_name = ''
    first_name = ''
    third_name = ''
    phone_num = ''
    print(f'Проверка выбора редактирования = {find_choice}')
    if find_choice == '1' or find_choice == '2':  # Поиск абонента для редактирования или удаления
        find_person(update, context)  # К меню запроса фамилии
        return SURNAME  # К вводу данных абонента
    elif find_choice == '3':  # Добавление абонента
        add_person(update, context)  # К меню запроса фамилии
        return SURNAME  # К вводу данных абонента
    elif find_choice == '4':
        update.message.reply_text(
            'Продолжить - введите y(es), выйти - введите q(uit)')
        return MAIN
    # elif find_choice == '4':
    #     return stop(update, context)
    update.message.reply_text(
        'Продолжить - введите y(es), выйти - введите q(uit)')
    return MAIN


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def add_person(update, context):
    print('Добавить запись в базу')
    update.message.reply_text('Введите фамилию')
    return
# ---------------------------------------------------------

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def find_person(update, context):
    update.message.reply_text('Введите искомую фамилию')
    return
# ---------------------------------------------------------

#   |   message: 1 / 2 / 3
#  \/   pointer: SURNAME


def edit_person(update, context):
    global find_choice
    # global active_base
    global person_id
    global second_name
    global first_name
    global third_name
    global phone_num
    global changed_person
    sur = update.message.text  # Получаем данные на абонента (любые)
    if find_choice == '1':  # Если "Удалить"
        update.message.reply_text(f'Удаляем абонента "{sur}"')
        remove_person(sur)
        update.message.reply_text(
            'Продолжить - введите y(es), выйти - введите q(uit)')
        return MAIN
    if find_choice == '2' or find_choice == '3':  # Если "Редактировать" или "Добавить"
        if second_name == '':  # Если фамилию ещё не вводили, то сохраняем фамилию
            second_name = sur  # в переменную (при вводе нового абонента)
            if find_choice == '2':  # Если "Редактировать",
                person_id = get_person_id(sur)  # то сохраняем ID
            elif find_choice == '3':  # Если "Добавить",
                # то присваиваем индекс на 1 больше последнего в базе
                person_id = str(int(active_base[-1][0]) + 1)
            update.message.reply_text('Введите имя абонента ')
            return SURNAME

        elif first_name == '':
            first_name = sur  # Сохраняем имя в переменную
            update.message.reply_text('Введите отчество абонента ')
            return SURNAME

        elif third_name == '':
            third_name = sur  # Сохраняем отчество в переменную
            update.message.reply_text('Введите телефон абонента ')
            return SURNAME

        else:
            phone_num = sur  # Сохраняем телефон в переменную

            # Сохраняем в кортеж данные абонента
            changed_person = (person_id, ' '+second_name,
                              ' '+first_name, ' '+third_name, ' '+phone_num)

            # Удаляем найденную запись по индексу и по этому же индексу
            # сохраняем кортеж в телефонный справочник (если редактируем абонента)
            if find_choice == '2':
                for person in active_base:  # Перебираем базу в поисках индекса абонента с введенной фамилией
                    if person[1].strip() == second_name.strip():
                        person_index = active_base.index(person)
                        # Удаляем найденную запись по индексу
                        active_base.remove(person)
                        # Вставляем на её место вновь сформированную запись
                        active_base.insert(person_index, changed_person)
                        update.message.reply_text(
                            f'Абонент "{second_name}" отредактирован')
            # Если новый абонент, то добавляем его в конец базы
            elif find_choice == '3':
                # Добавляем в базу нового абонента
                active_base.append(changed_person)
                update.message.reply_text(
                    f'Абонент "{second_name}" внесён в справочник')
            update.message.reply_text(
                'Продолжить - введите y(es), выйти - введите q(uit)')
            return MAIN


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def remove_person(sur):
    print('Удалить запись из базы')
    for person in active_base:
        if person[1].strip() == sur.strip():
            active_base.remove(person)
    return
# -------------------------------------------------------------

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def get_person_id(sur):
    print('Получаем id по фамилии')
    for person in active_base:
        if person[1].strip() == sur.strip():
            return person[0]
    return True
# -------------------------------------------------------------

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def show_phones(update: Update, context: CallbackContext):
    for el in active_base:
        update.message.reply_text(f'{el}')
    return
# -----------------------------------------------------------

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def save_phones(update: Update, context: CallbackContext):
    with open('base.csv', 'w') as file:
        for el in active_base:
            print(el)
            file.write(
                f'{el[0]};{el[1]};{el[2]};{el[3]};{el[4]}\n')
            # f'{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n')
    update.message.reply_text('Сохранили справочник')
    return
# ------------------------------------------------------
