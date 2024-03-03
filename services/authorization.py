from services.google_sheets import get_sheet, authorization
from telebot import types

# Предполагаем, что у нас есть структура данных для хранения состояния авторизации пользователей
authorized_users = {}


def authorize_contact(message, bot):
    global authorized_users
    phone_number = ''.join(filter(str.isdigit, message.contact.phone_number))
    sheet = get_sheet(authorization)

    try:
        # Поиск номера телефона в листе авторизации
        cell = sheet.find(phone_number)
        if cell:
            # Если номер найден, извлекаем информацию о пользователе
            user_name = sheet.cell(cell.row, 1).value  # Имя пользователя находится в первой колонке
            user_role = sheet.cell(cell.row, 3).value  # Роль пользователя находится в третьей колонке

            # Сохраняем статус авторизации пользователя
            authorized_users[message.chat.id] = {"name": user_name, "role": user_role}

            # Создаем разметку клавиатуры с кнопкой "Начать упаковку"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(types.KeyboardButton('Начать упаковку'))  # Добавляем кнопку начала упаковки

            # Отправляем сообщение об успешной авторизации с кнопкой начала упаковки
            bot.send_message(message.chat.id,
                             f"Авторизация прошла успешно. Ваше имя: {user_name}. Ваша роль: {user_role}.",
                             reply_markup=markup)
        else:
            # Если номер не найден, сообщаем об этом пользователю
            bot.send_message(message.chat.id, "Номер телефона не найден в системе. Авторизация не выполнена.")
    except Exception as e:
        print(f"Ошибка при авторизации: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при авторизации. Пожалуйста, попробуйте позже.")


def check_authorization_status(user_id):
    # Проверка, авторизован ли уже пользователь
    return user_id in authorized_users
