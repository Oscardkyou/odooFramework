# add_product_handler.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

class AddProductHandler:
    async def handle(self, message: types.Message, state: FSMContext):
        await message.answer("Введите данные товара в следующем формате:\n"
                             "Название, Описание")

        # Ожидание ответа от пользователя
        await YourStateEnum.YOUR_STATE_NAME.set()

# Добавьте необходимые импорты для вашего проекта
# from services import ProductService

# Создание экземпляра обработчика
add_product_handler = AddProductHandler()

# Регистрация обработчика команды
dp.register_message_handler(add_product_handler.handle, Command("add_product"))
