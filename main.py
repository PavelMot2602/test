from loader import bot
from commands import gen_markup
from telebot import custom_filters
import custom_handlers

"""Импортируем с других модулей все, что нужно для запуска бота и выполняем проверку имени файла"""
if __name__ == '__main__':
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    gen_markup(bot)
    bot.infinity_polling()
