from telegram import Update

# from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
# import bot_commands as bott


from bot_commands import *
from bot_token import *

# updater = Updater('5709545953:AAGln6vXYqUeWbBR-Q4N1R6YrmA9OVQDxss')
updater = Updater(BOT_TOKEN)

dp = updater.dispatcher

# Диалог калькулятора
# ===========================================================
calculator = ConversationHandler(
    # Точка входа в диалог. Выводит меню-подсказку
    entry_points=[CommandHandler('calc', calc_start)],

    states={
        # Получает пример, вычисляет и выводит ответ и меню "продолжить / выйти"
        COUNT: [MessageHandler(Filters.text, calculate)],
        # Функция читает ответ на второй вопрос и завершает диалог.
        CONT: [MessageHandler(Filters.text, calc_cont)],
    },

    fallbacks=[CommandHandler('stop', stop)]
)

# Диалог конвертора
# ===========================================================
convertor = ConversationHandler(
    # Точка входа в диалог.
    entry_points=[CommandHandler('conv', conv_start)],

    states={
        # Выбираем систему счисления
        SYST: [MessageHandler(Filters.text, conv_num_sys)],
        # Функция читает выбор пользователя
        DBIN: [MessageHandler(Filters.text, dec_to_bin)],
        # Функция читает введенное число и выдаёт результат конвертирования
        DOCT: [MessageHandler(Filters.text, dec_to_oct)],
        # Функция читает введенное число и выдаёт результат конвертирования
        DHEX: [MessageHandler(Filters.text, dec_to_hex)],
        # Выход из конвертора
        STOP: [MessageHandler(Filters.text, stop)],
    },

    fallbacks=[CommandHandler('stop', stop)]
)

# Диалог телефонного справочника
# ================================================================
phones_list = ConversationHandler(
    # Ничего не получает в ответ, передаёт управление следующему пункту (return 1 etc.),
    # но предварительно отрабатывает свой код
    entry_points=[CommandHandler('phone', phone_command)],

    states={
        # Основное меню справочника
        MAIN: [MessageHandler(Filters.text, main_menu)],
        # Выбор действий со справочником
        CHOICE: [MessageHandler(Filters.text, main_menu_choice)],
        # Найти абонента
        FIND: [MessageHandler(Filters.text, edit_book_choice)],
        # Ввести фамилию, имя, отчество и телефон абонента
        SURNAME: [MessageHandler(Filters.text, edit_person)],
        # Выход из справочника
        STOP: [MessageHandler(Filters.text, stop)],
    },

    fallbacks=[CommandHandler('stop', stop)]
)


dp.add_handler(calculator)  # Ожидание вызова калькулятора
dp.add_handler(convertor)  # Ожидание вызова конвертора
dp.add_handler(phones_list)  # Ожидание вызова калькулятора

dp.add_handler(CommandHandler("hi", hi_command))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("time", time_command))

print('Server start')

updater.start_polling()
updater.idle()
