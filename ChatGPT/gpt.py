import telebot
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

bot_token = "6136271584:AAG1rcLOfbvQ0RV5FlEpf0wVFGxPiZf6M5E"

bot = telebot.TeleBot(bot_token)

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


@bot.message_handler(commands=['start'])
def say_welcome(messege):
    user = messege.from_user
    bot.send_message(messege.chat.id, f'salom {user.first_name} ')


def chatbot(prompt):
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")

    bot_output = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    bot_response = tokenizer.decode(bot_output[0], skip_special_tokens=True)
    return bot_response


@bot.message_handler(func=lambda message: True)
def chat_handler(message):
    bot_response = chatbot(message.text)
    bot.send_message(message.chat.id, bot_response, reply_to_message_id=message.message_id)


if __name__ == '__main__':
    bot.infinity_polling()
