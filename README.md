# Fulfillment Efficiency Bot

Этот проект представляет собой бота, который контролирует эффективность процесса упаковки товаров в фулфилмент-центре. Вместо управления процессом упаковки, бот фиксирует начало и окончание работы сотрудника, вычисляет продолжительность работы и оценивает эффективность сотрудника на основе этих данных.

## Функционал и возможности бота:

1. **Начало упаковки товара:**
    - Сотрудник фулфилмента нажимает кнопку "Начать упаковку" в боте, когда начинает работу над упаковкой товара.
    - Бот стартует таймер и фиксирует время начала работы.

2. **Завершение упаковки товара:**
    - По окончании работы сотрудник нажимает кнопку "Закончить упаковку" в боте.
    - Бот останавливает таймер, фиксирует время окончания работы и вычисляет продолжительность работы сотрудника.

3. **Оценка эффективности работы:**
    - На основе времени работы бот вычисляет эффективность работы сотрудника.
    - Данные об эффективности сохраняются в Google Sheets для последующего анализа и принятия управленческих решений.

4. **Анализ и управление персоналом:**
    - На основе данных, собранных ботом, руководство фулфилмент-центра может делать выводы об эффективности работы сотрудников.
    - По итогам месяца можно принимать решения о премировании наиболее эффективных сотрудников или обучении менее продуктивных.

## Установка и настройка:

1. Склонируйте репозиторий:

git clone https://github.com/yourusername/fulfillment_efficiency_bot.git


2. Установите необходимые зависимости:

pip install -r requirements.txt


3. Получите токен бота Telegram и запишите его в файл `data/token.json.`

4. Создайте и настройте файл `data/googledata.json` с данными авторизации для доступа к Google Sheets API.

5. Запустите бота:

python main.py


## Структура проекта:

1. **bot/**
   - **\_\_init\_\_.py**: Файл инициализации Python-пакета.
   - **constants.py**: Содержит константы, используемые в боте.
   - **handlers.py**: Обработчики сообщений для бота.
   - **main.py**: Основной файл, запускающий бота и настраивающий его обработчики.
   - **utils.py**: Утилиты и вспомогательные функции.

2. **data/**
   - **googledata.json**: Данные авторизации для доступа к Google Sheets API.
   - **token.json**: Токен для доступа к API Telegram.

3. **requirements.txt**: Зависимости проекта.

4. **services/**
   - **\_\_init\_\_.py**: Инициализация Python-пакета для директории `services`.
   - **authorization.py**: Модуль для работы с авторизацией пользователей.
   - **google_sheets.py**: Модуль для взаимодействия с Google Sheets API.
   - **packing.py**: Модуль для управления процессом упаковки товаров.


## Благодарности

Спасибо за использование Fulfillment Efficiency Bot! Приятного пользования!
