# add_act_handler.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

class AddActHandler:
    async def handle(self, message: types.Message, state: FSMContext):
        await message.answer("Введите данные акта изменения свойств товара в следующем формате:\n"
                             "Склад откуда, Новый склад, Товар, Количество, Назначаемый статус, Расходы/поступления")

        # Ожидание ответа от пользователя
        await YourStateEnum.YOUR_STATE_NAME.set()

# Добавьте необходимые импорты для вашего проекта
# from services import PropertyChangeActService

# Создание экземпляра обработчика
add_act_handler = AddActHandler()

# Регистрация обработчика команды
dp.register_message_handler(add_act_handler.handle, Command("add_act"))
