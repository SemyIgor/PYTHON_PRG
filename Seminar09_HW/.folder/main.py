
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Привет, {update.effective_user.first_name} !')


app = ApplicationBuilder().token(
    "5709545953:AAGln6vXYqUeWbBR-Q4N1R6YrmA9OVQDxss").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("calc", calc_command))

print('Server start')

app.run_polling()
