from loader import bot
from telebot.types import Message
from commands import gen_markup


@bot.message_handler(func=lambda message: message.text == 'кнопка 3')
def get_image(message: Message) -> None:
    """Импортируем все, что нужно для отправки сообщения в тг-боте.
    Функция для работы второй кнопки, создаем переменные для текста и ссылки на фото, дальше отправляем их
    в сообщении. Подключаем клавиатуру с кнопками"""
    text = 'Красивый вид на природу'
    url = ('https://polinka.top/uploads/posts/2023-06/1685662686_polinka-top-p-krasivie-kartinki-prirodi-peizazhi-'
           'krasivo-7.jpg')
    bot.send_photo(
        message.chat.id,
        photo=url,
        caption=text,
        reply_markup=gen_markup(bot)
    )
