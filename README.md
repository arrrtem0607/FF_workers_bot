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

1.1 Склонируйте репозиторий:
```
git clone https://токен@github.com/arrrtem0607/FF_workers_bot.git
#введите токен вашего github
# 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 
Токен для Артема
```

1.2 Перейти в рабочую директорию:
```
cd FF_workers_bot
git checkout develop
```
2. Установите необходимые зависимости:
```
pip install -r requirements.txt
```

4. Получите токен бота Telegram и запишите его в файл `data/token.json.`

5. Создайте и настройте файл `data/googledata.json` с данными авторизации для доступа к Google Sheets API.
   
7. Создайте виртуальное окружение
```
virtualenv --python=/usr/bin/python3.12 myenv
```

8. Запустите бота из корневой директории:
```
cd /root/FF_workers_bot
tmux new -s botSession #для запуска беспрерывной сессии терминала botSession это название сессии
cd /root/FF_workers_bot
source myenv/bin/activate
python -m bot.main
```

9. Для дальнейшего подключения к непрерывной сессии:
```
tmux ls
tmux attach -t [session-name]
```
для завершение процесса
```
tmux ls
tmux kill-session -t [session-name]
```


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
   - **Фотоотчет о проделанное работе**: После окончания работ сотрудники должны присылать фотографии выполненной работы.
   - **Кнопка о количестве выявленного брака на этапе упаковки**: Сотруднику после конца упаковки вылезает сообщение о количестве упакованного товара, а так же о количестве забракованного товара. Эта информация автоматически добавляется в таблицу остатов товара и вычитается из общего доступного остатка для упаковки. Результат - более автоматический и системный подсчет брака.
   - **Коэфициент рабочего времени**: Сумма всех упаковок за определенный период / Количество рабочих часов по графику = Коэфициент занятости. Далее этот коэфициент занятости будет делитсься на чистую стоимость упаковки и таким образом будем получать реальную стоимость упаковки каждого из товаров. При этом нет жесткой слежки за курением и обедами, кто как хочет ходит курить или обедать, просто это будет в худшую сторону сказываться на коэфциенте.
   

2. **Геймификация**
   - **Уведомления после окончания упаковки**: Уведомления о том, что сотрудник побил свой собственный рекорд или наооборот, что в прошлый раз он поработал получше. Результаты текущей упаковки сравниваются с рекордами и нормативами. Если упаковщик сделал рекордное количества товаров - ему приходит уведомление о поздравлении. Всем остальным сотрудника тоже приходят уведомление об успехах этого сотрудника, чтобы они могли поздравить. Таким образом коллектив будет сближаться и конкурировать между собой - улучшая общую производительность.
   - **Таблица рекордов**: Доска почета, где будут показаны самые лучшие упаковщик и лучшее время. Кнопка, по которой будут открываться рекорды среди команды упаковщиков. Чтобы опять же можно было похвастаться или посмотреть сколько тебе нужно прибавить в скорости, чтобы подняться в таблицу лидеров по упаковке. Наверное эта информация тоже должна храниться в какой-то БДшке
   - **Нормативы**: Система званий. За конкретные достижения - нужно начислять звания. Эти звания будут видны всем сотрудникам, для того, чтобы они могли гордиться и хвастаться какими-то достижения (как система бейджей на платформе школы). Должна быть кнопка - показать мои звания, посмотреть звания кого-то и тд
   - **Выслуга лет**: Контроль за тем, какой период времени человек работает в нашей компании. За каждый пройденный этап тоже будет какая-то плюшка. Возможные этапы (1 месяц, 3 месяца, 6 месяцев, год, 1,5 года и тд). Обязательно уведомления администраторскому составу.
   

3. **Удобство работы**:
   - **Видео ТЗ на упаковку**: Сотрудники должны получать четкое ТЗ перед упаковкой. Не только в виде текста, но и в видеоформате. Нужно организовать какую-то базу данных, в которую мы сможем загружать видеоинструкции об упаковке новых товаров. Это облегчит работу новых сотрудников и не будет занимать время работы старых сотрудников для объяснения рабочих процессов новым.
   - **Уведомления о начале упаковки**: Администратору будут приходить уведомления о том, что сотрудник начал и закончил упаковку/погрузку. Для того, чтобы сложнее было обмануть и закончить работу чуть раньше/позже

4. **Функционал**
   - **Кнопка "ушел на погрузку/разгрузку" для грузчиков**: для удобства работы упаковщиков-грузчиков. Чтобы таймер упаковки останавливался во время погрузки разгрузки, время погрузки засчитывалось в рабочее время и не влияло на время "прогулов".
   - **Коэфициент "лентяйства" и учет времени прогулов**: Время прогулов - это время во время рабочего дня (с 9 до 19), в которое фактически работа не велась. Сюда нужно учитывать время перекуров, обедов, чаепитий, любой другой траты времени на нерабочие процессы. При этом знать что именно делали сотрудники в данные промежутки времени не нужно и неэтично. Нам не особо интересно сколько времени они были в туалете, сколько обедали и курили. Важно лишь то, что они не работали. Идея - вычитать из полного рабочего дня (10 часов) все время затраченное на работу (работа это упаковка или погрузка, в будущем вохможно будут и другой функционал). Соответвенно нужен функционал, который складывает все рабочее время за период, высчитывает из полного рабочего дня - чистое рабочее время и получается то самое время прогулов. Далее высчитывается коэфициент лентяйства. Отношение рабочего времени к нерабочему. Если сотрудник 5 часов работал и 5 часов "прогуливался", коэфициент "лентяйства" будет 1. Так как оплата за работу у нас не сделаьная, а почасовая, то чистое время сотрудника с коэфициентом 1 для нас будет стоить в 2 раза дороже, чем обычное время работы (так как оплачивается как чистое рабочее, так и прогулочное время). Этот коэфициент можно будет использоваться при подсчете стоимости на одну упаковку. Если сотрудник пакует товар 60 минут, это значит, что стоимость упаковки 1 товара равна стоимости часа рабочего времени сотрудника. Но если его коэфициент "лентяйства" равен 1, то на каждый рабочий час, он час "прогуливает" и стоимость это часа тоже должна быть учтена. Фактическая стоимость упаковки 1 товра тогда равна не стоимости часа, а стоимости 2 часов. 
   - **Функицонал администрации**: кнопка просмотра статистики работы , кнопка назначнения работы (чтобы администратор сам мог запускать таймер работы)
   - **Интеграция с таблицей очереди на упаковку**: сотрудник не сам выбирает товар, который хочет упаковать, а выбирает его из предложенных. Товары предлагаются из таблицы очереди на упаковку (https://docs.google.com/spreadsheets/d/1p0Q2K0-0e1adi12SEGd1sLF247AFJtiaoYH-5mlAvsY/edit#gid=32954266)
   - **Кнопка печати ШК**: автоматизировать запрос ШК. Бот должен автоматически подключатся к принетеру печати шк, сотрудник вводит необходимое количество, принетер печатет. Все проиходит без участия администратора


## Баги:
    - 1) Не появляется кнопка, если ты уже авторизован
    - 2) Непонятно как учитывать время палетирования. Пока просто не учитываем
    - 3) Нерегламентированно в какое время нажимать кнопку упаковки
   

## Благодарности

Спасибо за использование Fulfillment Efficiency Bot! Приятного пользования!
