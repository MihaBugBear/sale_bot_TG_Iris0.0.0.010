import telebot

TOKEN = '7119454159:AAEEHdEeZHqIFO2heibmv5gliwWBJZBr5oM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, "привет")

if __name__ == '__main__':
    bot.infinity_polling()