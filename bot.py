from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import settings
"""
CommandHandler - обработчик сообщений (только команды)
MessageHandler - обработчик всех сообщений (текст, картинки, аудио, видео)
"""

logging.basicConfig(filename='bot.log',level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
"""Level - уровень важности сообщений: 
debug - самый подробный
INFO - информационные сообщения
Warning - предупреждения, но не ошибки
Error - неустранимые ошибки
Format - указываем, какие данные выводятся в логе
"""

"""Можно использовать прокси для обхода блокировок (при необходимости)"""
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

"""
update - информация, которая нам пришла из телеги
context - с помощью этого можем обращаться к боту
"""
def greet_user(update, context):
    print('Вызван /start')
    print(update)
    update.message.reply_text("Здравствуй, пользователь!")

def talk_to_me(update,context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
def main():
    mybot = Updater(settings.API_KEY, use_context=True) # можно добавить request_kwargs=PROXY

    dp = mybot.dispatcher #чтобы каждый раз не писать длинное название
    dp.add_handler(CommandHandler('start', greet_user)) #добавляем к диспетчеру обработчика (название без слэша)
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) #ставим после CommandHandler, чтобы он не перехватывал в том числе команды

    logging.info('Бот стартовал')
    mybot.start_polling() #регулярные обращения в ТГ за обновлениями
    mybot.idle() #бот не выключается без команды

"""Нельзя вызывать функции на верхнему уровне, так как при импорте нашего бота функция сразу запустится и положит весь код"""
#main()
if __name__ == "__main__":
    main()
