from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import datetime
# from myBot import


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5916744952:AAH2Lnu_ZyUhZyKQeHZKD7mg0DzqJID0RwI").build()

async def hello(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}')

async def time_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now()}')

async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help\n')

async def sum_command(update: Update, context: CallbackContext):
    # log(update, context)
    # msg = update.message.text
    # items = msg.split()
    # print(msg)
    # x = int(items[1])
    # y = int(items[2])
    # await update.message.reply_text(f'{x} + {y} = {x + y}')
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(input())
    y = int(input())
    update.message.reply_text(f'{x} + {y} = {x+y}')
def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()


app.add_handler(CommandHandler('hello', hello))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))

print('server start')

app.run_polling()