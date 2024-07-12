from loader import bot
from telebot.types import Message
from config.config import sh
from commands import gen_markup


@bot.message_handler(func=lambda message: message.text == 'кнопка 4')
def get_element(message: Message) -> None:
    """Импортируем все, что нужно для отправки сообщения в тг-боте.
    Подключаем гугл таблицу и выводим значение ячейки А2. Подключаем клавиатуру с кнопками"""
    ws = sh.sheet1
    cell = ws.cell(1, 2).value
    bot.send_message(
        message.chat.id,
        f'Элемент таблицы А2: {cell}',
        reply_markup=gen_markup(bot)
    )
