import telebot
from telebot import types


bot=telebot.TeleBot('5543210761:AAER7-nSoSMMAvHxHZb9r6LUesEPjB8-ct4')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет! \nВведи команду /help и узнай что я умею')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '/calc - воспользуйся калькулятором')

@bot.message_handler(commands=['calc'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Калькулятор")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Калькулятор":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Сложение")
        item2=types.KeyboardButton("Вычитание")
        item3=types.KeyboardButton("Деление")
        item4=types.KeyboardButton("Умножение")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id,'Какую арифметическую операцию желаете выполнить?',reply_markup=markup)
    if message.text=="Сложение":
        bot.send_message(message.chat.id, 'Введите через пробел 4 числа:')
        summ_message(message)

def summ_message(message):
    msg = message.text
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[3])
    y2 = float(items[4])
    com_dig1 = complex(x1, y1)
    com_dig2 = complex(x2, y2)
    message.reply_text(f'{com_dig1} - {com_dig2} = {com_dig1 - com_dig2}')
bot.infinity_polling()