from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config.config import DEFAULT_COMMANDS


def gen_markup(bot):
    """Создаем кнопки, которые будут работать в боте"""
    button_1 = KeyboardButton(text='кнопка 1')
    button_2 = KeyboardButton(text='кнопка 2')
    button_3 = KeyboardButton(text='кнопка 3')
    button_4 = KeyboardButton(text='кнопка 4')
    button_5 = KeyboardButton(text='кнопка 5')
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    return keyboard
