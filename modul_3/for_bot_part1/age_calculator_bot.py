import telebot

BOT_TOKEN = "5742470161:AAHaOL-OHGEa1unT6l1oU5SZRnPUIWpdfD4"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id,
                     f"Assalomu Aleykum {user.first_name} \n"
                     f"yoshinggiz nechchida ekanligini bilmoqchimisiz unda\n"
                     f"yilinggizni bizga jo'nating?")


@bot.message_handler(func=lambda message: int)
def echo_meesage_age(message):
    msg = message.text
    bot.reply_to(message, f"Siz - {2023 - int(msg)} yoshda ekansiz.")


if __name__ == "__main__":
    print("Starting...")
    bot.infinity_polling()