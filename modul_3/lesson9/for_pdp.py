from telebot import *
from commands import Studendregistration
from telebot import custom_filters
from telebot.types import ReplyKeyboardRemove
from uiteles import *
import os
import csv
from commands import get_result_btn

Api = '5998055063:AAFhU6NBUQ0ZRBfc8FvibdPLTN54NJxFdfQ'
bot = telebot.TeleBot(Api)


@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, f'Salom {message.from_user.first_name}  Pdp academy botga xush kelbsiz 👋🏻')
    bot.register_next_step_handler(message, step1)
    print(message)


@bot.message_handler(commands=['registr'])
def step1(message):
    bot.send_message(message.chat.id, 'Ismingzni kriting : ')
    bot.set_state(message.from_user.id, Studendregistration.first_name, message.chat.id)


@bot.message_handler(state=Studendregistration.first_name)
def first_name(message):
    bot.send_message(message.chat.id, 'Familyangizni kriting : ')
    bot.set_state(message.from_user.id, Studendregistration.last_name, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['first_name'] = message.text


@bot.message_handler(state=Studendregistration.last_name)
def get_phone(message):
    item = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item.add(types.KeyboardButton('Share phone', request_contact=True))
    bot.send_message(message.chat.id, 'Telefon raqamizni kiriitng: ', reply_markup=item)
    bot.set_state(message.from_user.id, Studendregistration.phone, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_name'] = message.text


@bot.message_handler(state=Studendregistration.phone, content_types=['contact'])
def age_get(message):
    bot.send_message(message.chat.id, 'Yoshingizni kriting :', reply_markup=ReplyKeyboardRemove())
    bot.set_state(message.from_user.id, Studendregistration.age, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.contact.phone_number


@bot.message_handler(state=Studendregistration.age)
def get_location(massege):
    item = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item.add(types.KeyboardButton('Share location', request_location=True))
    bot.send_message(massege.chat.id, 'Joylashuvingizni kriting :', reply_markup=item)
    bot.set_state(massege.from_user.id, Studendregistration.location, massege.chat.id)
    with bot.retrieve_data(massege.from_user.id, massege.chat.id) as data:
        data['age'] = massege.text
    with bot.retrieve_data(massege.from_user.id, massege.chat.id) as data:
        data['location'] = massege.location
        bot.register_next_step_handler(massege, say_win)


@bot.message_handler(content_types=['text'])
def say_win(message):
    chat_id = message.chat.id
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['course'] = message.text
        msg = "Quyidagi ma'lumotlar qa'bul qilindi:\n"
        msg += f"Fullname: {data.get('first_name')} {data.get('last_name')}\n"
        msg += f"Phone: {data.get('phone')}\n"
        msg += f"Age: {data.get('age')}\n"
        msg += "ushbu malumotlar saqlansinmi ?\n"
        msg += "ha -> ✅\n"
        msg += "yo'q -> ❌\n"
        msg+=f'chat id {chat_id}'
        button_yes = types.InlineKeyboardButton('Ha', callback_data='cb_Ha')
        button_no = types.InlineKeyboardButton('Yoq', callback_data='cb_No')
        keybord = types.InlineKeyboardMarkup()
        keybord.add(button_yes)
        keybord.add(button_no)
        bot.send_message(chat_id, text=msg, reply_markup=keybord)
        bot.register_next_step_handler(message, callback_query)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        print(data)
        if call.data == "cb_Ha":
            row = data
            header = list(data.keys())

            save_registration(
                header ,row
            )

            bot.send_message(call.message.chat.id, "malumotlar saqlandi")

        elif call.data == "cb_No":
            bot.send_message(call.message.chat.id, "malumotlar saqlanmadi")
        bot.delete_state(call.from_user.id, call.message.chat.id)


# @bot.message_handler(content_types=['text'])
# def next_step(message):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['course'] = message.text
#         msg = "Quyidagi ma'lumotlar qa'bul qilindi:\n"
#         msg += f"Fullname: {data.get('first_name')} {data.get('last_name')}\n"
#         msg += f"Phone: {data.get('phone')}\n"
#         msg += f"Age: {data.get('age')}\n"
#         msg += f"Language: {data.get('language')}\n"
#         msg += f"Course: {data.get('course')}\n"
#         msg += "ushbu malumotlar saqlansinmi ?\n"
#         msg += "ha -> ✅\n"
#         msg += "yo'q -> ❌"
#         bot.send_message(message.chat.id, msg)


bot.add_custom_filter(custom_filters.StateFilter(bot))


def my_command():
    return [
        types.BotCommand("/registr", "registration")
    ]


if __name__ == '__main__':
    bot.set_my_commands(my_command())
    bot.infinity_polling()
