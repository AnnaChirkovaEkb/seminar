from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, Updater
import datetime
# from myBot import TOKEN


async def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}')


async def time_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now()}')


async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help\n/sum\n')


async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    print(msg)
    x = int(items[0])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()


app = ApplicationBuilder().token('5916744952:AAH2Lnu_ZyUhZyKQeHZKD7mg0DzqJID0RwI').build()

app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))


print('server start')

app.run_polling()