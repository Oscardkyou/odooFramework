from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor

API_TOKEN = ''  # Замените на свой токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

if __name__ == '__main__':
    from aiogram import executor
    from aiogram import types

    executor.start_polling(dp, skip_updates=True)
