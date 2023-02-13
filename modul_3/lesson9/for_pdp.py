import telebot
from environs import Env
from telebot import types
from telebot.types import BotCommand

env = Env()
env.read_env()

API_TOKEN = env('bot_pdp')
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def say_hello(meesage):
    chat_id = meesage.chat.id
    user = meesage.from_user
    bot.send_message(chat_id, f'salom {user.first_name} Pdp regstration bot ga hush kelibsiz 👋🏻   ')
    bot.send_message(chat_id, 'Menu 👉🏻 /registratsiya')


@bot.message_handler(commands=['registratsiya'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Jo'natish", request_contact=True)
    markup.add(item1)
    bot.send_message(message.chat.id, 'Telifon raqamingizni jonating ! ', reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def get_phone(message):
    # print(message.phone_number)
    bot.send_message(message.chat.id, "Muvofaqqiyatli qo'shildi !")



def my_commands():
    return [
        BotCommand('/start', 'starting bot'),
        BotCommand('/registratsiya', 'menu button'),
    ]


if __name__ == '__main__':
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
