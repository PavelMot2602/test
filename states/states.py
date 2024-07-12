from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    """Создаем статус для сохранения места нашей остановки в работе тг-бота, а именно для ввода даты"""
    date_check = State()
