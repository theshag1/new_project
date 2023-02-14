import telebot
from modul_3.forbotparrt1.todo_bot import Env
import csv


env = Env()
env.read_env()

API_TOKEN = env('bot_token2')
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, f"salom {user.first_name} 👋🏻 ")
    bot.send_message(chat_id, 'Vazifa yaratish uchun /add yozing')

@bot.message_handler(commands=['add'])
def add_task_handler(message):
    bot.send_message(message.chat.id, 'Vazifa yaratish uchun yozib yuboring')
    bot.register_next_step_handler_by_chat_id(message, get_task_handlr)


@bot.message_handler(content_types=['text', 'voice', 'photo'])
def get_task_handlr(message):  #
    if message.content_type != 'text':
        bot.send_message(message.chat.id, 'Invalid format  restart 👉🏻 /start  ')
    bot.send_message(message.chat.id, 'Qoshildi !')


if __name__ == '__main__':
    bot.infinity_polling()
