from telebot import types
from services.authorization import authorize_contact, check_authorization_status
from services.packing import start_packing, end_packing, count_packing_data, packing_status
from services.google_sheets import get_products_list
from telebot.types import ReplyKeyboardRemove

packing_start_times = {}


def setup_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Авторизация')
        welcome_text = "Привет! Я бот фулфилмент-центра. Для начала работы необходимо авторизоваться."
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Авторизация")
    def request_contact(message):
        if check_authorization_status(message.chat.id):
            bot.send_message(message.chat.id, "Вы уже авторизованы.")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(types.KeyboardButton('Начать упаковку'))
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            button_phone = types.KeyboardButton(text="Отправить мой номер телефона", request_contact=True)
            markup.add(button_phone)
            bot.send_message(message.chat.id, "Пожалуйста, поделитесь своим номером телефона для авторизации в системе",
                             reply_markup=markup)

    @bot.message_handler(content_types=['contact'])
    def contact_handler(message):
        authorize_contact(message, bot)

    @bot.message_handler(
        func=lambda message: message.text == "Начать упаковку" or message.text == "Упаковать следующий товар")
    def request_sku_input(message):
        bot.send_message(chat_id=message.chat.id, text="Пожалуйста, введите артикул товара, который "
                                                       "собираетесь упаковывать. "
                                                       "SKU должен быть числом.", reply_markup=ReplyKeyboardRemove())

        bot.register_next_step_handler(message, process_sku_input)

    def process_sku_input(message):
        try:
            sku = int(message.text.strip())
        except ValueError:
            bot.send_message(message.chat.id, "SKU должен быть числом. Пожалуйста, введите корректный SKU.")
            bot.register_next_step_handler(message, process_sku_input)
            return

        products = get_products_list()
        product = next((p for p in products if p['id'] == sku), None)

        if product:
            # Здесь вызываем функцию для добавления записи о начале упаковки в Google Sheets
            start_packing(message.chat.id, sku, bot)

            # Обновляем интерфейс, изменяя кнопки
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Закончить упаковку')
            bot.send_message(message.chat.id, f"Упаковка товара {product['name']} начата. \n\nТЗ: {product['task']}",
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Товар с таким SKU не найден. Попробуйте ввести SKU еще раз.")
            bot.register_next_step_handler(message, process_sku_input)

    @bot.message_handler(func=lambda message: message.text == 'Закончить упаковку')
    def handle_end_packing(message):
        if check_authorization_status(message.chat.id):
            bot.send_message(chat_id=message.chat.id, text="Введите количество упакованных товаров:",
                             reply_markup=ReplyKeyboardRemove())
            bot.register_next_step_handler(message, end_packing, bot)
        else:
            bot.send_message(message.chat.id, "Пожалуйста, авторизуйтесь перед завершением упаковки.")

    @bot.message_handler(func=lambda message: packing_status.get(message.chat.id) == 'awaiting_quantity')
    def handle_quantity_input(message):
        count_packing_data(message, bot)

    @bot.callback_query_handler(func=lambda call: call.data == "start_next_packing")
    def start_next_packing(call):
        bot.answer_callback_query(call.id, "Начните упаковку следующего товара.")
        # Можете добавить здесь логику для начала упаковки следующего товара
        bot.send_message(call.message.chat.id, "Пожалуйста, введите артикул товара, который собираетесь упаковывать.")
        sku = int(call.message.text.strip())
        start_packing(call.message.chat.id, sku, bot)
