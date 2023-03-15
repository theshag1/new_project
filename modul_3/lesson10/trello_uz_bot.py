import telebot
from telebot import custom_filters
import commands
from utils import get_member_tasks_message, \
    chek_chat_id_
from keybords import get_inline_bords_btn, get_lists_btn, get_inline_lists_btn, get_members_btn, get_boards_btn
from fortrello import TrelloManager
from states import CreateNewTask
from datetime import *
from queries import *
import psycopg2
from psycopg2.extras import RealDictCursor
import queries
from sync import sync_board, sync_lists
from oz import connection
# from keybords import get_inline_bords_btn ,get_inline_lists_btn , get_members_btn , get_lists_btn

# get_inline_boards_btn

from environs import Env

env = Env()
tokenn = env('BOT_TOKEN')

# bot = telebot.TeleBot(Api_token)

state_stroge = telebot.storage.StateMemoryStorage()
bot = telebot.TeleBot(tokenn, state_storage=state_stroge, parse_mode="html")


# /start
@bot.message_handler(commands=["start"])
def welcome(message):
    user = message.from_user
    bot.send_message(message.chat.id, commands.WELCOME_MSG)


@bot.message_handler(commands=["help"])
def say_help(message):
    bot.send_message(message.chat.id,
                     'Trello uz bot sizga juda kop qlayliklar tugdirishi mumkn \n misol uchun vazifaalarni bolib berish \n yangi list , doska yaratsh vaxokozo')


# /cancel
@bot.message_handler(commands=["cancel"])
def welcome(message):
    bot.send_message(message.chat.id, commands.CANCEL)


@bot.message_handler(commands=["register"])
def registration(message):
    chat_id = message.chat.id
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.get_chat_id, (chat_id,))
        user = cur.fetchall()
        if not user:
            chat = message.from_user
            cur.execute(queries.write_user, (chat_id, chat.first_name, chat.last_name, chat.username))
            connection.commit()
            bot.send_message(message.chat.id, commands.SEND_TRELLO_USERNAME)
            bot.register_next_step_handler(message, get_trello_username)
        else:
            bot.send_message(message.chat.id, commands.ALREADY_REGISTERED)


# Trello username
def get_trello_username(message):
    with connection.cursor() as cur:
        trello_username = message.text
        trello_id = TrelloManager(trello_username).get_member_id()
        cur.execute(
            queries.update_user_trellochat_id, (trello_username, trello_id, message.chat.id)
        )
        connection.commit()
    bot.send_message(message.chat.id, commands.ADD_SUCCESSFULLY)


@bot.message_handler(commands=["sync"])
def sync_trello_handler(message):
    chat = message.chat.id
    bot.send_message(message.chat.id, commands.SYNC_START)
    # sync Trello
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.get_chat_id, (chat,))
        users = cur.fetchall()
        for user in users:
            sync_board(user.get('trello_username'))
    bot.send_message(message.chat.id, commands.SYNC_END)


@bot.message_handler(commands=['boards'])
def send_task(message):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.get_chat_id, (message.chat.id,))
        user = cur.fetchone()
        trello_usernae = user.get('trello_username')
        print(user.get('id'))
    if trello_usernae:
        bot.send_message(
            message.chat.id, commands.SELECT_BOARD,
            reply_markup=get_inline_bords_btn(user.get('id'), 'task_board')
        )
    else:
        bot.send_message(message.chat.id, commands.TRELLO_USERNAME_NOT_FOUND)


@bot.callback_query_handler(lambda c: c.data.startswith("task_board"))
def get_board_lists(call):
    message = call.message
    chat_id = message.chat.id
    board_id = call.data.split("_")[2]
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.get_chat_id, (chat_id,))
        user = cur.fetchone()
        if user:
            print(board_id , 'bu c')
            print(user.get('id') , 'bu id')
            cur.execute(queries.get_user_by_board_id, (board_id ,user.get('id')))
            cards = cur.fetchall()
            print(cards)
            if cards:
                bot.send_message(chat_id, get_member_tasks_message(cards, ))
            else:
                bot.send_message(chat_id, commands.NO_TASKS)
        else:
            bot.send_message(chat_id, commands.TRELLO_USERNAME_NOT_FOUND)




@bot.message_handler(commands=["new"])
def create_new_task(message):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.get_chat_id, (message.chat.id))
        users = cur.fetchall()
        if not users:
            bot.send_message(message.chat.id, commands.TRELLO_USERNAME_NOT_FOUND)
        else:
            print('topild')


@bot.message_handler(state=CreateNewTask.list)
def get_list_id_for_new_task(message):

    # list_id = call.data.split("_")[3]
    bot.send_message(message.chat.id, commands.TASK_NAME)
    bot.set_state(message.from_user.id, CreateNewTask.name, message.chat.id)
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #     data["task_list_id"] = list_id


@bot.message_handler(state=CreateNewTask.name)
def get_task_name(message):
    bot.send_message(message.chat.id, commands.TASK_DESC)
    bot.set_state(message.from_user.id, CreateNewTask.description, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["task_name"] = message.text
        params = {
            "name": data["name"],
            "desc": data["desc"],
        }


@bot.callback_query_handler(lambda c: c.data.startswith("new_task_member_"))
def get_member_id(call):
    message = call.message
    member_id = call.data.split("_")[3]
    bot.send_message(message.chat.id, commands.TASK_LABELS)
    bot.set_state(message.from_user.id, CreateNewTask.members, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["member_id"] = member_id
        print(data)


bot.add_custom_filter(custom_filters.StateFilter(bot))

my_commands = [
    telebot.types.BotCommand("/start", 'Botdan foydalinishni boshlash'),
    telebot.types.BotCommand("/register", "Registration o'tish"),
    telebot.types.BotCommand('/tasks', 'Vazifalar jadvali'),
    telebot.types.BotCommand("/new", "Yangi vazifa yaratish"),
    telebot.types.BotCommand("/boards", "Trello vazifalarini Qdirish"),
    telebot.types.BotCommand("/cancel", "Vzifani Bekor qilish"),
    telebot.types.BotCommand("/help", "Yordam"),
    telebot.types.BotCommand("/sync", "Sinxorizatsiya ")
]

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(my_commands)
    bot.infinity_polling()
