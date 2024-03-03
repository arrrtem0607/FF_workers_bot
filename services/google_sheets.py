import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Глобальные переменные
client = None
authorization = "Авторизация"
products = "Товарная матрица"
packing_tracker = "Трекер"


def initialize_google_sheets():
    global client

    # Инициализация клиента Google Sheets
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("../data/googledata.json", scopes)
    client = gspread.authorize(creds)


def get_sheet(sheet_name):
    global client
    if client is None:
        initialize_google_sheets()
    document_link = "https://docs.google.com/spreadsheets/d/1iqIx6elY_pO4NdKUz-U_8f6J-zfclUMMP_0rqfN3Rpo/edit#gid=0"
    try:
        document = client.open_by_url(document_link)
        sheet = document.worksheet(sheet_name)
        return sheet
    except gspread.exceptions.WorksheetNotFound:
        print(f"Лист с именем '{sheet_name}' не найден в документе.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при получении листа: {e}")
        return None


# Пример функции для работы с листом товаров
def get_product_by_sku(sku):
    sheet = get_sheet(products)
    product_list = sheet.get_all_records()
    for product in product_list:
        if product['SKU'] == sku:
            return product
    return None


# Пример функции для добавления записи в трекер упаковки
def add_packing_record(user_id, sku, start_time, end_time, quantity_packed):
    sheet = get_sheet(packing_tracker)
    sheet.append_row([user_id, sku, start_time, end_time, quantity_packed])


def get_products_list():
    products_sheet = get_sheet(products)  # Используем ранее инициализированный лист продуктов
    products_records = products_sheet.get_all_records()

    products_list = []
    for record in products_records:
        product_info = {
            "name": record['Товар'],  # или другой ключ, соответствующий вашей структуре
            "id": record['SKU'],  # или другой ключ, соответствующий вашей структуре
            "task": record['ТЗ']  # или другой ключ, соответствующий вашей структуре
        }
        products_list.append(product_info)

    return products_list
