# apply_act_handler.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

class ApplyActHandler:
    async def handle(self, message: types.Message, state: FSMContext):
        await message.answer("Введите номер акта для применения")

        # Ожидание ответа от пользователя
        await YourStateEnum.YOUR_STATE_NAME.set()

# Добавьте необходимые импорты для вашего проекта
# from services import ActApplicationService

# Создание экземпляра обработчика
apply_act_handler = ApplyActHandler()

# Регистрация обработчика команды
dp.register_message_handler(apply_act_handler.handle, Command("apply_act"))
