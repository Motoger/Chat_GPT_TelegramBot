import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6125835287:AAEX1IPu2jdI92jg1aEu1Gsf762Z94I4duU'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
