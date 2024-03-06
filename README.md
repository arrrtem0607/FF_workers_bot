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

'''
git clone https://github.com/yourusername/fulfillment_efficiency_bot.git
'''


2. Установите необходимые зависимости:

'''
pip install -r requirements.txt
'''

4. Получите токен бота Telegram и запишите его в файл `data/token.json.`

5. Создайте и настройте файл `data/googledata.json` с данными авторизации для доступа к Google Sheets API.

6. Запустите бота из корневой директории:

'''
cd /root/FF_workers_bot
tmux new -s botSession
cd /root/FF_workers_bot
source myenv/bin/activate
python -m bot.main
'''


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

## Планируемые обновления:

1. **Отчетность сотрудников**
   - **Что-то**: После окончания работ сотрудники должны присылать фотографии выполненной работы.
   - **Кнопка о количестве выявленного брака на этапе упаковки**: Сотрудник нажимает эту кнопку, вводит количество забракованного товраа. Эта информация автоматически добавляется в таблицу остатов товара и вычитается из общего доступного остатка для упаковки
   - **Инфорация об обедах и перекурах**: Функционал, который позволит отслеживать чистое рабочее время сотрудника и время, потраченное на перекуры и обеды
   - **Время выхода на рабочее место, время начала  конца смены, чтобы отслеживать опоздания**
   - **Коэфициент рабочего времени**: Сумма всех упаковок за определенный период / Количество рабочих часов по графику = Коэфициент занятости. Далее этот коэфициент занятости будет делитсься на чистую стоимость упаковки и таким образом будем получать реальную стоимость упаковки каждого из товаров. При этом нет жесткой слежки за курением и обедами, кто как хочет ходит курить или обедать, просто это будет в худшую сторону сказываться на коэфциенте.
   

2. **Геймификация**
   - **Уведомления после окончания упаковки**: Уведомления о том, что сотрудник побил свой собственный рекорд или наооборот, что в прошлый раз он поработал получше
   - **Таблица рекордов**: Доска почета, где будут показаны самые лучшие упаковшиик и лучшее время
   - **Нормативы**: Ввести нормативы, при выполнении которых у упаковщиков будут повышаться звания. За это можно начислять какие-то плюшки.
   - **Выслуга лет**: Контроль за тем, сколько человек работает в нашей компании. За каждый пройденный этап тоже будет какая-то плюшка. Возможные этапы (1 месяц, 3 месяца, 6 месяцев, год, 1,5 года и тд)
   

3. **Удобство работы**:
   - **Видео ТЗ на упаковку**: Сотрудники должны получать четкое ТЗ перед упаковкой. Не только в виде текста, но и в видеоформате. Это облегчит работу новых сотрудников и не будет занимать время работы старых сотрудников для объяснения рабочих процессов новым
   - **Увеломления о начале упаковки**: Администратору будут приходить уведомления о том, что сотрудник начал работу

4. **Функционал**
   - **Кнопка "ушел на погоузку/разгрузку" для грузчиков**: для удобства работы упаковщиков-грузчиков. Чтобы таймер останавливался во время погрузки разгрузки
   - **Кнопка "перекур" и "обед"**: возможный функионал, надл обдумать. по идее было бы хорошо отслеживать рабочее и нерабочее время сотрудников
   - **Функицонал администрации**: кнопка просмотра статистики работы , кнопка назначнения работы (чтобы администратор сам мог запускать таймер работы)


## Баги:
    - 1) Не появляется кнопка, если ты уже авторизован
    - 2) Неправильно считается стоиомсть часа
    - 3) Непонятно как учитывать время палетирования. Пока просто не учитываем
    - 4) Нерегламентированно в какое время нажимать кнопку упаковки
   

## Благодарности

Спасибо за использование Fulfillment Efficiency Bot! Приятного пользования!
