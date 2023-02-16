import telebot
from telebot import *


Api_token  = '6125284208:AAHp77bpqAmY0Ey_1bWGOG6Nz3CQcP-sw-c'

bot = telebot.TeleBot(Api_token)


@bot.message_handler(commands=['start'])
def say_hello(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id , f'Salom {user.first_name}  Trello uz botga hush kelbsiz ')


if __name__ == '__main__':
    bot.infinity_polling()