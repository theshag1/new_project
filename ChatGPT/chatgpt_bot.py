import telebot
import torch
from torch import res
from torch import res
from torch.utils import model_zoo
# Telegram bot tokenini kiritish
TOKEN = '6136271584:AAG1rcLOfbvQ0RV5FlEpf0wVFGxPiZf6M5E'

# Botni yaratish
bot = telebot.TeleBot(TOKEN)

# ChatGPT modelini yuklash
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load('chatbot_model.pth', map_location=device)
model.eval()


# Botga xabar kelganda javob berish
@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
    input_text = message.text
    # ChatGPT modeliga kiritilgan xabarni o'zgartirish
    input_text = "chatbot: " + input_text.strip().lower() + "\n"
    # ChatGPT modeli orqali javob generatsiyasi
    output_text = generate_response(input_text)
    # Chatbot javobini yuborish
    bot.send_message(message.chat.id, output_text)


# Telegram botni ishga tushirish
bot.polling()
