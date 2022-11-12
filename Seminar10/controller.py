import spy as spy
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot

from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
CHOICE, PLAY, FIN = range(3)
TURNS_NUMBER = 7  # За сколько ходов приблизительно должна закончится игра
sweets_on_the_table = 0
sweets_at_once = 0
gif_counter = 0

reply_keyboard = [['/help', '/stop']]
markup = ReplyKeyboardMarkup(
    reply_keyboard, one_time_keyboard=False, resize_keyboard=True)


# Entry point
def start_sweets(update, context):
    global gif_counter
    gif_counter = 0
    spy.log(update, context)
    update.message.reply_text('Хочешь сыграть?')
    start_menu(update, context)  # Выводит начальное меню (и подсказку "help")
    update.message.reply_text(
        'Скажи, сколько у нас на столе лежит конфет?', reply_markup=markup)
    return CHOICE


def start_menu(update, context):
    update.message.reply_text(
        'OK! Моя игра - мои правила:\n'
        '- по очереди берём со стола конфеты;\n'
        '- тот, кто заберёт последние конфеты, тот заберёт всё!\n'
        '- мой ход первый.\n')
    return


# CHOICE
def how_mach_takes(update, context):
    global sweets_on_the_table
    global sweets_at_once
    # ==============================
    input_msg_str = update.message.text
    input_msg_cut = input_msg_str.strip()
    if input_msg_cut == "/stop":
        return finish_game(update, context)
    elif input_msg_cut == "/help":
        start_menu(update, context)
        update.message.reply_text(
            'Скажи, сколько у нас на столе лежит конфет?', reply_markup=markup)
        return CHOICE
    # Здесь проверка на то, что введено число
    elif not input_msg_cut.isdigit():
        update.message.reply_text('Уважаемый, надо бы число...\n'
                                  'Попробуй ещё раз: сколько на столе конфет?')
        return CHOICE
    # ----------------------------------------------
    sweets_on_the_table = int(input_msg_cut)
    if sweets_on_the_table < 14:
        update.message.reply_text(
            f'{sweets_on_the_table} конфет мало, играть не интересно :(')
        return finish_game(update, context)
    # Определяет, сколько максимально можно брать конфет за ход
    sweets_at_once = (sweets_on_the_table // TURNS_NUMBER)
    # Делаем первый ход
    if (sweets_on_the_table % (sweets_at_once + 1)) != 0:
        print(f'sweets_at_once = {sweets_at_once}')
        update.message.reply_text(f'За один ход можно брать не более {sweets_at_once}шт. конфет\n'
                                  f'Я беру {sweets_on_the_table % (sweets_at_once + 1)}шт. конфет\n'
                                  f'На столе осталось {sweets_on_the_table - (sweets_on_the_table % (sweets_at_once + 1))}шт. конфет\n'
                                  f'Твой ход, брать не более {sweets_at_once}шт. конфет')
        sweets_on_the_table = sweets_on_the_table - \
            (sweets_on_the_table % (sweets_at_once + 1))
        return PLAY
    else:
        # Если изначально инициатива у игрока, то даём ему конфетку и делаем первый ход
        sweets_on_the_table = sweets_on_the_table - 1
        update.message.reply_text(f'Угостись 1 конфеткой - всё равно остальные будут моими :)\n'
                                  f'Итак, на столе {sweets_on_the_table}шт. конфет\n'
                                  f'За один ход можно брать не более {sweets_at_once}шт. конфет\n'
                                  f'Я беру {(sweets_on_the_table) % (sweets_at_once + 1)}шт. конфет\n'
                                  f'На столе осталось {(sweets_on_the_table) - ((sweets_on_the_table) % (sweets_at_once + 1))}шт. конфет\n'
                                  f'Твой ход, брать не более {sweets_at_once}шт. конфет')
        sweets_on_the_table = (sweets_on_the_table) - \
            ((sweets_on_the_table) % (sweets_at_once + 1))
        return PLAY


# PLAY
def turns(update, context):
    global sweets_on_the_table
    global sweets_at_once
    pl_turn = update.message.text
    player_turn = pl_turn.strip()
    if player_turn == "/stop":
        return finish_game(update, context)
    elif player_turn == "/help":
        start_menu(update, context)
        update.message.reply_text(f'Понятно? Сейчас на столе лежит {sweets_on_the_table} конфет\n'
                                  f'За ход можно взять от 1 до {sweets_at_once} конфет\n'
                                  f'Итак, сколько ты возьмёшь конфет?', reply_markup=markup)
        return PLAY
    # Здесь проверка на то, что введено число
    elif not player_turn.isdigit():
        update.message.reply_text('Уважаемый, надо бы число...')
        return PLAY
    else:
        # Рассчитываем и делаем ход
        player_turn = int(player_turn)
        update.message.reply_text(f'Ты взял {player_turn}шт. конфет')
        if sweets_at_once < player_turn or player_turn <= 0:
            update.message.reply_text(
                'Эй! Мы так не договаривались\n''Попробуй ещё')
            context.bot.send_document(
                chat_id=update.effective_chat.id, document="https://gifgive.com/wp-content/uploads/2021/12/dumaet.gif")
            return PLAY
        else:
            return comp_turn(player_turn, update, context)


def comp_turn(player_turn, update, context):
    global sweets_on_the_table
    global sweets_at_once
    global gif_counter
    # После правильного хода противника осталось 0 конфет
    if (sweets_on_the_table - player_turn) == 0:
        update.message.reply_text('Ого! Да ты выиграл! Поздравляю!')
        context.bot.send_document(
            chat_id=update.effective_chat.id, document="https://gifgive.com/wp-content/uploads/2021/12/aplodismenty.gif")
        return finish_game(update, context)
    # Игрок пытается забрать конфет больше, чем осталось на столе
    elif (sweets_on_the_table - player_turn) < 0:
        update.message.reply_text('Эй! Здесь нет столько конфет! Переходи')
        return PLAY
    # Анализируем ход игрока и делаем свой
    else:
        sweets_on_the_table = sweets_on_the_table - player_turn
        bots_sweets = sweets_on_the_table % (sweets_at_once + 1)
        # Если возможен выигрышный ход, то выигрываем
        if sweets_on_the_table <= sweets_at_once:
            update.message.reply_text(
                f'Я забираю последние {bots_sweets} конфет, и ты проиграл.\n'
                f'Но не расстраивайся: можешь забрать все конфеты себе - \n'
                'бот конфеты не любит :)')
            return finish_game(update, context)
        # За один ход до последнего даём игроку шанс на выигрыш
        elif (sweets_on_the_table // (sweets_at_once + 1)) == 1:
            bots_sweets = player_turn if (
                sweets_at_once - player_turn) == 0 else 1
            update.message.reply_text(
                f'На столе у нас...{sweets_on_the_table} конфет')
            sweets_on_the_table = sweets_on_the_table - bots_sweets
            update.message.reply_text(f'Я возьму {bots_sweets} конфет')
            # Исключаем повторное появление гифки, если игрок первый раз не использовал шанс
            if gif_counter == 0:
                gif_counter = -1
                context.bot.send_document(
                    chat_id=update.effective_chat.id, document="https://gifgive.com/wp-content/uploads/2021/12/bolshoj-smajlik.gif")
            update.message.reply_text(f'Упс! Я ошибся ;) и у тебя есть шанс...\n'
                                      f'Итого у нас на столе {sweets_on_the_table} конфет\n'
                                      f'Твой ход. Возьми конфет не более {sweets_at_once}')
            return PLAY
        # Обычный ход бота
        else:
            update.message.reply_text(
                f'Хорошо! На столе у нас...{sweets_on_the_table} конфет\n'
                f'Я возьму {bots_sweets} конфет')
            sweets_on_the_table = sweets_on_the_table - bots_sweets
            update.message.reply_text(
                f'Итого у нас на столе {sweets_on_the_table} конфет\n'
                f'Твой ход. Возьми конфет не более {sweets_at_once}')
    return PLAY


def finish_game(update, context):
    print('На выход!')
    stop(update, context)
    return ConversationHandler.END


def stop(update, context):  # Завершение работы вызванной функции
    spy.log(update, context)
    update.message.reply_text(
        "Всего доброго!", reply_markup=ReplyKeyboardRemove())
    return


def help_command(update, context):
    spy.log(update, context)
    update.message.reply_text(
        f'/help - this menu\n/sweets - play candies')
