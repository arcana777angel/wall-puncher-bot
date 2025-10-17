from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "7551870189:AAFfHdBVvWxDDwHP_nvtg3CjwZxSRFqhs9g"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

user_coins = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_coins[user_id] = 0
    await message.reply("💥 Ударь по стене — получи монетку! Нажми /punch")

@dp.message_handler(commands=['punch'])
async def punch(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    user_coins[user_id] += 1
    await message.reply(f"👊 Ты ударил по стене! Монеток: {user_coins[user_id]}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
