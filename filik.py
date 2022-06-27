from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from finder import*
import csv
from encodings import utf_8
from data_input import*
# pip install python-telegram-bot - загрузить библиотеку

path_file_token = r'C:\Users\Pavel\Desktop\Study\project\token.txt'
with open(path_file_token, 'r') as data:
    for line in data:
        str_token = line

bot = Bot(token=str_token)
updater = Updater(token=str_token, use_context=True)
dispatcher = updater.dispatcher

FUNCTIONS = "/find_by_number -- найти абонента по номеру\n" \
            "/find_by_name -- найти абонента по имени\n" \


CHOICE = 0

def start(update, _):
    reply_keyboard = [['Найти по ФИО', 'Найти по номеру']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'По каким параметрам будем искать?'
        'Команда /cancel, чтобы прекратить поиск.\n\n',
        reply_markup=markup_key,)
    return CHOICE


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Меня создали в муках")


def message(update, context):
    global find_type
    find_type = update.message.text
    if find_type == 'Найти по ФИО':
        context.bot.send_message(update.effective_chat.id, "Введите ФИО: ")
    if find_type == 'Найти по номеру':
        context.bot.send_message(update.effective_chat.id, "Введите номер: ")
    return ConversationHandler.END


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, 'Такая команда мне не знакома. Вот что я могу:')
    context.bot.send_message(update.effective_chat.id, FUNCTIONS)

def cancel(update, _):
    update.message.reply_text(
        'До свидания!',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.regex('^(Найти по ФИО|Найти по номеру)$'), message)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )


message_handler = MessageHandler(Filters.text, searching_sabscribers)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(message_handler)

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
unknown_handler = MessageHandler(Filters.command, unknown)
message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print("server_started")

updater.start_polling()
updater.idle()




# def start(update, context):
#     arg = context.args
#     if not arg:
#         context.bot.send_message(update.effective_chat.id, "Привет, я телефонный справочник\nВот мои возможности:")
#         context.bot.send_message(update.effective_chat.id, FUNCTIONS)
#     else:
#         context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


# def message(update, context):
#     text = update.message.text
#     if text.lower() == 'привет':
#         context.bot.send_message(update.effective_chat.id, "Привет, я телефонный справочник\nВот мои возможности:")
#     else:
#         context.bot.send_message(update.effective_chat.id, 'Я тебя не понимаю, может ты имел ввиду:')
#     context.bot.send_message(update.effective_chat.id, FUNCTIONS)