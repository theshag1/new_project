import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '5698075014:AAH2z_6iOGjhznanCI7N8Mvvw6cP3kLYI4M'

openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.9,
        top_p=1.0,
        max_tokens=1000,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=['You:']
    )
    await message.answer(response['choices'][0]['text'])


executor.start_polling(dp, skip_updates=True)
