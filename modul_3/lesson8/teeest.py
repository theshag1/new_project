import telebot
from telebot import types

BOT_TOKEN = "5944021178:AAHu1UylG5y3S4z478z2UMXYPjCc9gCn444"
bot = telebot.TeleBot(BOT_TOKEN)

key = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text="Amharic", callback_data="am")
btn2 = types.InlineKeyboardButton(text=" Arabic", callback_data="ar")
btn3 = types.InlineKeyboardButton(text=" Hindi", callback_data="hi")
key.add(btn1, btn2, btn3)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # here is my question, what does i have to write in text variable ?
    text = call.message.chat.text
    # ?????????
    if call.data == "am":
        translator = Translator()
        translation = translator.translate(text, dest="am")
        bot.send_message(call.message.chat.id, text)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, 'HELLO!!! send a message!')


@bot.message_handler(func=lambda call: True)
def choose(message):
    bot.send_message(message.chat.id, "select your language:", reply_markup=key)


bot.infinity_polling()