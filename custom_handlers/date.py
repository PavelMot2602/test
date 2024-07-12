from loader import bot
from telebot.types import Message
from states.states import States
from telebot.types import ReplyKeyboardRemove


@bot.message_handler(func=lambda message: message.text == 'кнопка 5')
def date_entry(message: Message):
    """
    Функция для отправки работы пятой кнопки бота, а также для смены статуса, чтобы в дальнейшем проверить дату на
    верность ее ввода
    """
    bot.send_message(
        message.chat.id,
        'Пожалуйста, введите дату в формате ГГГГ-ММ-ДД'
    )
    bot.set_state(message.from_user.id, States.date_check, message.chat.id)
