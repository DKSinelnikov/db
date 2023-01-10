from saving_the_token import token
from db import add_message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
import json

from aiogram.types import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)



bot = Bot(token=token)
dp = Dispatcher(bot)
button1 = KeyboardButton('заказ')
keyboard = ReplyKeyboardMarkup()
keyboard.add(button1)
button2 = KeyboardButton('жалоба')
keyboard.add(button2)


bad_words = ["дурак", "идиот", 'дьявол', 'чёрт', 'хрень', 'фигня']


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("I glad to see you!")
    user_id = message.from_user.id
    with open("users.json", "r") as f:
        user_data = json.load(f)
    if user_id not in user_data:
        user_data.append(user_id)
        with open("messages.json", "w") as f:
            json.dump(user_data, f, ensure_ascii=False, indent=4)

for word in bad_words:
    @dp.message_handler(filters.Text(contains=word, ignore_case=True))
    async def bad_message(msg: types.Message):
        await bot.send_message(msg.from_user.id, "Не ругайтесь. ")


@dp.message_handler(commands=['hello'])
async def menu(message: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("yandex.ru", url='https://ya.ru'))
    markup.add(InlineKeyboardButton('отмена', callback_data='delete'))








@dp.message_handler(filters.Text(contains='жалоба', ignore_case=True))
async def confort_user(msg: types.Message):
    await bot.send_message(msg.from_user.id, "На что у вас есть жалоба? Ваш ответ должен содержать, я жалуюсь на... ")


@dp.message_handler(filters.Text(contains='я жалуюсь на', ignore_case=True))
async def confort_user(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Хорошо, мы поняли вас. Мы попытаемся исправить эту ошибку. Спасибо, что вы помогаете нам быть лучше! ")


@dp.message_handler(filters.Text(contains='заказ', ignore_case=True))
async def viches(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Извините, сейчас мы не можем принять заказ. Попытайтесь заказать завтра. ")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    user_id = msg.from_user.id
    text = msg.text
    add_message(user_id, text)


@dp.message_handler()
async def kyeword(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Выберете действие', reply_markup=keyboard)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
