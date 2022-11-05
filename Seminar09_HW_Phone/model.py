from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import logger as log


# ++++++++++++++++++++++++++++++++++++++
def get_csv_file():
    print('Загружаем csv файл')
    active_base = log.get_csv_data()
    return active_base
# --------------------------------------
