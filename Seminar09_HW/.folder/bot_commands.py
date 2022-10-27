import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from spy import *
import datetime


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
   #  update.message.reply_text(f'Привет, {update.effective_user.first_name} !')
    await update.message.reply_text(f'Привет, {update.effective_user.first_name} !')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
   #  update.message.reply_text(f'/help\n/hello\n/time\n/calc')
    await update.message.reply_text(f'/help\n/hello\n/time\n/calc')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
   #  update.message.reply_text(
   #      f'{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}:{datetime.datetime.now().time().second}:{datetime.datetime.now().today}')
    await update.message.reply_text(f'{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}:{datetime.datetime.now().time().second}:{datetime.datetime.now().today}')


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    res_ult = (msg[5:]).strip()
    res_ult = eval(res_ult)
    print(res_ult)
   #  update.message.reply_text(f'{res_ult}')
    await update.message.reply_text(f'{res_ult}')
