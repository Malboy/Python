from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/help\n/time\n/filter\n/calc')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def delete_some_useles_words(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    index = msg.find(' ')
    msg = msg[index + 1:]
    update.message.reply_text(f'{" ".join([i for i in msg.split() if "абв" not in i])}')

def calc_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Choose operation:\n/sum\n/sub\n/mult\n/div')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[3])
    y2 = float(items[4])
    com_dig1 = complex(x1, y1)
    com_dig2 = complex(x2, y2)
    update.message.reply_text(f'{com_dig1} + {com_dig2} = {com_dig1+com_dig2}')

def sub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[3])
    y2 = float(items[4])
    com_dig1 = complex(x1, y1)
    com_dig2 = complex(x2, y2)
    update.message.reply_text(f'{com_dig1} - {com_dig2} = {com_dig1 - com_dig2}')

def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[3])
    y2 = float(items[4])
    com_dig1 = complex(x1, y1)
    com_dig2 = complex(x2, y2)
    update.message.reply_text(f'{com_dig1} * {com_dig2} = {com_dig1 * com_dig2}')

def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[3])
    y2 = float(items[4])
    com_dig1 = complex(x1, y1)
    com_dig2 = complex(x2, y2)
    update.message.reply_text(f'{com_dig1} / {com_dig2} = {com_dig1 / com_dig2}')