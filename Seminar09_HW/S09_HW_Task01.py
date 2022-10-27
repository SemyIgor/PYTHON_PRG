# Следующие библиотеки получаем на pypi.org (см. здесь в файле main.py):
# from isOdd import isOdd
# from progress.bar import Bar
# import emoji
# import matplotlib # Система построения графиков и диаграмм в отдельном "окне"
# import time

# IS ODD
# Со строкой не работает.
# print(isOdd('1'))  # //=> true
# print(isOdd('5'))  # //=> true

# print(isOdd(1))  # //=> True
# print(isOdd(8))  # //=> False

# PROGRESS BAR
# bar = Bar('Processing', max=100)
# for i in range(100):
#     # Do some work
#     time.sleep(0.1)  # Задержка в секундах
#     bar.next()
# bar.finish()
# print('Процесс завершён !')

# print(emoji.emojize("Dont smoke :gift_heart:", language="alias"))
# print(emoji.emojize("Dont smoke :smoking:", language="alias"))
# print(emoji.emojize("Python is fun :broken_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# print(emoji.is_emoji("👍"))

# TELEGRAM BOT
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(
    "5709545953:AAGln6vXYqUeWbBR-Q4N1R6YrmA9OVQDxss").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
