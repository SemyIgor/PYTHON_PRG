from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove

from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters

import bot_token as bot
import controller as con

updater = Updater(bot.BOT_TOKEN)

dp = updater.dispatcher

sweets = ConversationHandler(
    # Точка входа в диалог. Выводит меню-подсказку
    entry_points=[CommandHandler('sweets', con.start_sweets)],

    states={
        # Переход к расчёту параметров игры и первого хода
        con.CHOICE: [MessageHandler(Filters.text, con.how_mach_takes)],
        # Обеспечиваем диалог в игре
        con.PLAY: [MessageHandler(Filters.text, con.turns)],
        # По алгоритму в это точку не попадаем, оставляем для проформы
        con.FIN: [MessageHandler(Filters.text, con.finish_game)],
    },

    fallbacks=[CommandHandler('stop', con.finish_game)]
)

dp.add_handler(sweets)
dp.add_handler(CommandHandler("help", con.help_command))
dp.add_handler(CommandHandler("stop", con.finish_game))  # Ожидание вызова игры


print('Server start')

updater.start_polling()
updater.idle()
