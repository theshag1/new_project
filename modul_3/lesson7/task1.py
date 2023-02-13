import telebot

API_TOKEN = '5742470161:AAHaOL-OHGEa1unT6l1oU5SZRnPUIWpdfD4'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, f'Salom  {user.first_name} 👋🏻')


if __name__ == '__main__':
    bot.infinity_polling()
