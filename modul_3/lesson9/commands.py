from telebot.handler_backends import State, StatesGroup
from telebot.types import (
    ReplyKeyboardRemove,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


class Studendregistration(StatesGroup):
    first_name = State(),
    last_name = State(),
    phone = State(),
    age = State(),
    location = State(),
    language = State(),
    course = State(),

RESULT = {
    "❌" : "no",
    "✅" : "yes"
}

def get_result_btn():
    result_inline_btn = InlineKeyboardMarkup()
    result_inline_btn.add(
        InlineKeyboardButton(list(RESULT.keys())[0], callback_data=f"result_{list(RESULT.keys())[0]}"),
        InlineKeyboardButton(list(RESULT.keys())[1], callback_data=f"result_{list(RESULT.keys())[1]}"),
    )
