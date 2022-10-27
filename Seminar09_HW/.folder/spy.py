import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open('db.csv', 'a')
    file.write(
        f'{datetime.datetime.now().time()}; {update.effective_user.id}; {update.effective_user.full_name}; {update.message.text}\n')
    file.close()
