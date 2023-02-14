import requests
import telebot
from environs import Env
import json

env = Env()
env.read_env()

Api = env('exchange_bot')
bot = telebot.TeleBot(Api)

KEY = 'gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR'
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={KEY}"
resp = requests.get(url)


@bot.message_handler(commands=['start'])
def say_data(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, f'salom {user.first_name}  👋🏻')
    bot.send_message(chat_id, 'Pul briligini tanlang : ')


@bot.message_handler(commands=['usdsom'])
def info(message):
    bot.send_message(message.chat.id , f'Aqsh dollari xajmini kriting :\nPlase input Use dollar:')
    bot.register_next_step_handler(message,exchangeusd)

@bot.message_handler(content_types=['text'])
def exchangeusd(message):
    msg =message.text
    msg = float(msg)
    som = 11400
    exchange = msg*som
    exchange =str(exchange)
    bot.send_message(message.chat.id ,f'{exchange} som')


@bot.message_handler(commands=['somusd'])
def info(message):
    bot.send_message(message.chat.id , f'Uzbekiston somini  kriting :\nPlase input Uzbekistan som :')
    bot.register_next_step_handler(message , exchangesom)

@bot.message_handler(content_types=['text'])
def exchangesom(message):
    msg =message.text
    msg = float(msg)
    som = 11.400
    exchange = msg/som
    exchange =str(exchange)
    bot.send_message(message.chat.id ,f'{exchange} usd')






if __name__ == '__main__':
    bot.infinity_polling()
