from loader import bot
from telebot.types import Message
from commands import gen_markup


@bot.message_handler(commands=['start'])
def welcome(message: Message) -> None:
    """Импортируем все, что нужно для отправки сообщения в тг-боте.
    Отправляем сообщение с приветствием, а также подключаем клавиатуру с кнопками"""
    bot.send_message(
        message.chat.id,
        'Рад приветствовать!',
        reply_markup=gen_markup(bot)
    )
