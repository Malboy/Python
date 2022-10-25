from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5617862152:AAHS48V0222nwJHzMouuONhs-fFaHRsi_lA')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('filter', delete_some_useles_words))
updater.dispatcher.add_handler(CommandHandler('calc', calc_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('sub', sub_command))
updater.dispatcher.add_handler(CommandHandler('mult', mult_command))
updater.dispatcher.add_handler(CommandHandler('div', div_command))

updater.start_polling()
updater.idle()