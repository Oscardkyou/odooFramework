from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor

API_TOKEN = 'YOUR_API_TOKEN'  # Замените на свой токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\nЯ бот для управления информационной системой маркировки товаров.\n"
                        "Для добавления товара введите /add_product\n"
                        "Для добавления акта изменения свойств товара введите /add_act\n"
                        "Для применения акта введите /apply_act")


@dp.message_handler(commands=['add_product'])
async def add_product(message: types.Message):
    """
    This handler will be called when user sends /add_product command
    """
    await message.reply("Введите название товара:")
    # Добавьте логику для обработки названия товара


@dp.message_handler(commands=['add_act'])
async def add_act(message: types.Message):
    """
    This handler will be called when user sends /add_act command
    """
    await message.reply("Введите данные акта изменения свойств товара:")
    # Добавьте логику для обработки данных акта


@dp.message_handler(commands=['apply_act'])
async def apply_act(message: types.Message):
    """
    This handler will be called when user sends /apply_act command
    """
    await message.reply("Введите данные акта для применения:")
    # Добавьте логику для применения акта


if __name__ == '__main__':
    from aiogram import executor
    from aiogram import types

    executor.start_polling(dp, skip_updates=True)
