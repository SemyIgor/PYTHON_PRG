import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(
        f'{datetime.datetime.now().today()}; {update.effective_user.id}; {update.effective_user.full_name}; {update.message.text}\n')
    file.close()
