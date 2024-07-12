import telebot
from config import config
from telebot.storage import StateMemoryStorage

"""Импортируем токен бота, а также функцию для сохранения статуса, чтобы в дальнейшем проверять дату"""
state_storage = StateMemoryStorage()
bot = telebot.TeleBot(config.BOT_TOKEN)
