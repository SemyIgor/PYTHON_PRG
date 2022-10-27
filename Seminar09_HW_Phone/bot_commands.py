import datetime
from telegram import Update
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

from spy import *
from phone import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет, {update.effective_user.first_name} !')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/help\n/hi\n/time\n/calc')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(
        f'{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}:{datetime.datetime.now().time().second}')


def calc_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    res_ult = (msg[5:]).strip()
    res_ult = eval(res_ult)
    print(res_ult)
    update.message.reply_text(f'{res_ult}')


def phone_command(update: Update, context: CallbackContext):
    log(update, context)
    con.run(update, context)  # Запускаем controller.py
    update.message.reply_text('Справочник приветствует тебя!')


# def start(update, context):
#     context.bot.send_message(update.effective_chat.id, 'Привет! Это бот )')
