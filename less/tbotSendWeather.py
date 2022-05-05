import telebot

bot = telebot.TeleBot("5125341770:AAF11nLzMCoeFV-gf96iL19hDyhOfidqo7g", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()