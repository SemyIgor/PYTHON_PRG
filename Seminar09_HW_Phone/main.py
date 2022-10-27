from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


updater = Updater('5709545953:AAGln6vXYqUeWbBR-Q4N1R6YrmA9OVQDxss')

dp = updater.dispatcher

dp.add_handler(CommandHandler("hi", hi_command))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("time", time_command))
dp.add_handler(CommandHandler("calc", calc_command))
dp.add_handler(CommandHandler("phone", phone_command))
# dp.add_handler(CommandHandler("phone", phone_command))

print('Server start')

updater.start_polling()
updater.idle()
