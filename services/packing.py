import time
import datetime
import uuid
from zoneinfo import ZoneInfo
from services.google_sheets import get_sheet, get_products_list, packing_tracker
from services.authorization import authorized_users
from datetime import datetime
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


# Global variables to keep track of the packing status
packing_start_info = {}
packing_status = {}
cnt = 2


def start_packing(user_id, sku, bot):
    global packing_start_info, cnt
    packing_id = str(uuid.uuid4())  # Генерация уникального ID для упаковки
    user_name = authorized_users.get(user_id, {}).get("name", "Неизвестный")
    product_info = next((item for item in get_products_list() if item["id"] == sku), None)
    if not product_info:
        bot.send_message(user_id, "Товар с таким SKU не найден.")
        return

    start_time = time.time()
    packing_start_info[user_id] = {"packing_id": packing_id, "start_time": start_time, "sku": sku, "product"
                                                                         "_name": product_info["name"], "row": cnt}

    tracker_sheet = get_sheet(packing_tracker)
    start_time = datetime.fromtimestamp(start_time, ZoneInfo("Europe/Moscow")).strftime('%Y-%m-%d %H:%M:%S')
    packing_data = [
        packing_id,
        user_name,
        product_info["name"],
        start_time,
        '',
        '',
        ''
    ]
    tracker_sheet.append_row(packing_data)
    cnt += 1


def end_packing(message, bot):
    global packing_start_info, packing_status
    user_id = message.chat.id
    packing_id = packing_start_info[user_id]['packing_id']
    if user_id not in packing_start_info:
        bot.send_message(user_id, "Начало упаковки для данного пользователя не было зафиксировано")
        return

    start_time = packing_start_info[user_id]['start_time']
    end_time = time.time()
    packing_duration = end_time - start_time
    salary = 3000  # TODO: внести зарплату в БД
    work_cost = (packing_duration/3600) * salary  # TODO: усовершенствовать функция подсчета стоимости работы

    tracker_sheet = get_sheet(packing_tracker)
    row_number = find_row_by_packing_id(tracker_sheet, packing_id)

    end_time_moscow = datetime.fromtimestamp(end_time, ZoneInfo("Europe/Moscow")).strftime('%Y-%m-%d %H:%M:%S')
    tracker_sheet.update_cell(row_number, 5, end_time_moscow)
    tracker_sheet.update_cell(row_number, 6, packing_duration)
    tracker_sheet.update_cell(row_number, 7, work_cost)

    count_packing_data(message, bot, packing_id)


def clear_packing_data(user_id):
    global packing_start_info, packing_status
    packing_start_info.pop(user_id, None)
    packing_status.pop(user_id, None)


def count_packing_data(message, bot, packing_id):
    user_id = message.chat.id
    quantity = message.text.strip()

    if not quantity.isdigit():
        bot.send_message(user_id, "Пожалуйста, введите числовое значение.")
        bot.register_next_step_handler(message, count_packing_data)  # Запрашиваем ввод ещё раз
        return

    try:
        tracker_sheet = get_sheet(packing_tracker)
        row_number = find_row_by_packing_id(tracker_sheet, packing_id)
        tracker_sheet.update_cell(row_number, 8, quantity)  # Обновляем количество в таблице
        bot.send_message(user_id, "Количество упакованных товаров сохранено. Упаковка завершена.")
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        next_packing_button = KeyboardButton("Упаковать следующий товар")
        markup.add(next_packing_button)
        bot.send_message(user_id, "Начать упаковать следующий товар?", reply_markup=markup)
    finally:
        clear_packing_data(user_id)


def find_row_by_packing_id(sheet, parametr):
    all_records = sheet.get_all_records()
    for index, record in enumerate(all_records, start=2):  # Начинаем с 2, т.к. 1 строка это заголовки
        if record.get('ID упаковки') == parametr:
            return index
    return None
