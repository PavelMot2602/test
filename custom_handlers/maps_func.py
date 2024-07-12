from loader import bot
from telebot.types import Message
from commands import gen_markup


@bot.message_handler(func=lambda message: message.text == 'кнопка 1')
def get_map(message: Message) -> None:
    """Импортируем все, что нужно для отправки сообщения в тг-боте.
    Фунция для кнопки 1, отправляем текст с ссылкой внутри. Подключаем клавиатуру с кнопками"""
    bot.send_message(
        message.chat.id,
        'Ссылка на карту по адресу г. Иркутск, ул. Ленина, 1\n'
        'https://yandex.ru/maps/63/irkutsk/house/ulitsa_lenina_1/ZUkCaAVnQEYEXUJvYWJzeHxiZwE=/'
        '?ll=104.279330%2C52.290139&z=17.14',
        reply_markup=gen_markup(bot)
    )
