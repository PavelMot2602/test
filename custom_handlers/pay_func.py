from loader import bot
from telebot.types import Message
from commands import gen_markup


@bot.message_handler(func=lambda message: message.text == 'кнопка 2')
def get_pay(message: Message) -> None:
    """Импортируем все, что нужно для отправки сообщения в тг-боте.
    Отправляем сообщение с ссылкой на оплату. Подключаем клавиатуру с кнопками"""
    bot.send_message(
        message.chat.id,
        'Ссылка на оплату\n'
        'https://yoomoney.ru/to/4100118745775434',
        reply_markup=gen_markup(bot)
    )
