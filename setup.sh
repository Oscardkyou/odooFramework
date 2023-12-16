#!/bin/bash

# Путь к папке проекта
PROJECT_PATH="./my_bot_project"

# Создание основной структуры проекта
mkdir -p $PROJECT_PATH
cd $PROJECT_PATH

# Создание директорий для модулей SOLID
mkdir -p core
mkdir -p entities
mkdir -p services
mkdir -p interfaces

# Создание файла для бота
touch bot.py

# Создание файла для хранения токена
touch .env

# Запись токена в .env
echo "API_TOKEN=YOUR_API_TOKEN" > .env

# Создание директории для хендлеров
mkdir -p handlers

# Создание файла для базовых хендлеров
touch handlers/base_handlers.py

# Создание файла для хендлера добавления товара
touch handlers/add_product_handler.py

# Создание файла для хендлера добавления акта
touch handlers/add_act_handler.py

# Создание файла для хендлера применения акта
touch handlers/apply_act_handler.py

# Создание файла для маршрутизации
touch routing.py

# Добавление базового кода в bot.py
echo -e "from aiogram import Bot, Dispatcher, types\nfrom aiogram.types import ParseMode\nfrom aiogram.contrib.middlewares.logging import LoggingMiddleware\nfrom aiogram import executor\n\nAPI_TOKEN = 'YOUR_API_TOKEN'  # Замените на свой токен\n\nbot = Bot(token=API_TOKEN)\ndp = Dispatcher(bot)\ndp.middleware.setup(LoggingMiddleware())\n\nif __name__ == '__main__':\n    from aiogram import executor\n    from aiogram import types\n\n    executor.start_polling(dp, skip_updates=True)" > bot.py

# Вывод завершения выполнения
echo "Структура проекта создана!"
