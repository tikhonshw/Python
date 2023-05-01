import time
import telebot
from telebot import types

bot = telebot.TeleBot('5482277086:AAH2ZZbmLM3d7B997GG3y5ai8v_0SO1ZnrQ') #АВЕТО
# bot = telebot.TeleBot("5125341770:AAF11nLzMCoeFV-gf96iL19hDyhOfidqo7g") #КДП

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['test'])
def start(message):
    mess = f'Проверка, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.from_user.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('photo.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Cool photo', parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить", url="https://ya.ru"))
    bot.send_message(message.chat.id, 'Cool photo', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Погода')
    start1 = types.KeyboardButton('Погода1')
    rasp = types.KeyboardButton('Расписание')


    markup.add(website, start, start1, rasp)
    bot.send_message(message.chat.id, 'Cool photo', reply_markup=markup)


bot.polling(none_stop=True)
