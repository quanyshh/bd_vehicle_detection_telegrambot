from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import token


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message.chat.id)
    await message.reply("Привет!\nЗдесь будут результаты распознавания техники")


if __name__ == '__main__':
    executor.start_polling(dp)