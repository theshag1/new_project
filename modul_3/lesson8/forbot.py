from environs import Env
import telebot
from translate import Translator
from telebot.types import BotCommand

env = Env()
env.read_env()

bot_token = env('translate_bot')
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, f"salom {user.first_name} 👋🏻\nUzbek➡️English /uzen\nEnglish➡️Uzbek /enuz")


@bot.message_handler(commands=['uzen'])
def translate_to_eng(message):
    chat_id = message.chat.id
    user = message.from_user
    msg = bot.send_message(chat_id, f'Yaxshi {user.first_name} endi menga Uzbekcha soz yuboring :  ')
    bot.register_next_step_handler(msg, tarjima_uz_en)


def tarjima_uz_en(message):
    trans = Translator(from_lang='Uzb', to_lang='en')
    translation = trans.translate(message.text)
    bot.reply_to(message, translation)


@bot.message_handler(commands=['enuz'])
def translate_to_eng(message):
    chat_id = message.chat.id
    user = message.from_user
    msg = bot.send_message(chat_id, f'Good {user.first_name} now send me from english word :  ')
    bot.register_next_step_handler(msg, translate_en_uz)


@bot.message_handler(func=lambda message: True)
def translate_en_uz(message):
    trans = Translator(from_lang='en', to_lang='Uzb')
    translation = trans.translate(message.text)
    bot.reply_to(message, translation)


def my_commad():
    return [
        BotCommand('/start', 'starting bot'),
        BotCommand('/uzen', 'uz -> en'),
        BotCommand('/enuz ', 'en -> uz')
    ]


if __name__ == '__main__':
    bot.set_my_commands(commands=my_commad())
    bot.infinity_polling()
