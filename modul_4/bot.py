import telebot
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import *

api = '6071943245:AAGBGkLAvdd8yq4RKXST-3VXlfnpX4rIPdI'

bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def say_hello(messege):
    user = messege.from_user
    bot.send_message(messege.chat.id, f'salom {user.first_name}')
    connection = psycopg2.connect(
        dbname='trello',
        user='postgres',
        password='12345',
        host='localhost',
        port=5432

    )
    cur = connection.cursor(cursor_factory=RealDictCursor)
    sql = "insert into save(name, chat_id, time) values ( %s, %s, %s)"
    cur.execute(sql, (user.first_name, messege.chat.id, datetime.now()))
    connection.commit()
    print(cur)


if __name__ == '__main__':
    bot.infinity_polling()
