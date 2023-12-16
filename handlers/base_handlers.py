# base_handler.py

from aiogram import Dispatcher

class BaseHandler:
    def __init__(self, dp: Dispatcher):
        self.dp = dp

    async def init_handlers(self):
        # обработчик команд добавить 
        pass
