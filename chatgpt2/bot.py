import telebot
import requests

# Telegram bot tokeni
TOKEN = '5853644779:AAGqUncbPcrOANe9lXjppo5Rok-U2uNLoTQ'

# ChatGPT API manzili
API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'
api_key = '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'
# Bot yaratish
bot = telebot.TeleBot(TOKEN)

# Xabar kelganda javob qaytarish
@bot.message_handler(func=lambda message: True)
def reply(message):
    # Foydalanuvchi xabarini olish
    text = message.text
    # ChatGPT API ga so'rov jo'natish
    response = requests.post(API_URL, headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }, json={
        'prompt': text,
        'max_tokens': 100,
        'temperature': 0.7
    })
    print(response)
    # API javobini olish
    if response.status_code == 200:
        response_text = response.json()['choices'][0]['text']
    else:
        response_text = 'Uzr, nima uchun javob bermayapti'
    # Foydalanuvchi uchun javobni yuborish
    bot.reply_to(message, response_text)

# Botni ishga tushirish
bot.polling(none_stop=True)
if __name__ == '__main__':
    bot.infinity_polling()




























































'''import telegram
import openai
from telegram.ext import Updater, MessageHandler, filters
import requests
from telegram import *
Token = '5853644779:AAGqUncbPcrOANe9lXjppo5Rok-U2uNLoTQ'
openai.api_key = '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'
enigine_id = 'text-davinci-003'
url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
updater = Updater(token=Token, use_contexte=True)


def reply(update, context):
    # Foydalanuvchi xabarini olish
    message = update.message.text
    # ChatGPT API ga so'rov jo'natish
    response = requests.post(url, headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai.api_key}'
    }, json={
        'prompt': message,
        'max_tokens': 100,
        'temperature': 0.7
    })
    # API javobini olish
    if response.status_code == 200:
        response_text = response.json()['choices'][0]['text']
    else:
        response_text = 'Uzr, nima uchun javob bermayapti'
    # Foydalanuvchi uchun javobni yuborish
    update.message.reply_text(response_text)

# MessageHandler qo'shish
updater.dispatcher.add_handler(MessageHandler(filters.text ,filters.command, reply))

# Botni ishga tushirish
updater.start_polling()
updater.idle()'''