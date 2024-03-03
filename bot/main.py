# bot/main.py
import telebot
from bot.handlers import setup_handlers
import json

def main():
    with open('../data/token.json') as file:
        data = json.load(file)
    bot = telebot.TeleBot(data['TOKEN'])
    setup_handlers(bot)
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()
