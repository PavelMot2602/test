from loader import bot
from telebot.types import Message
from config.config import sh
from states.states import States
from datetime import datetime
from commands import gen_markup


@bot.message_handler(state=States.date_check)
def date_check(message: Message):
    """Проверяем дату на верность ввода"""
    try:
        check = datetime.strptime(message.text, '%Y-%m-%d').date()
        """Подключаем гугл-таблицу и заносим ее в первую свободную ячейку, если дата введена верно. 
        Подключаем клавиатуру с кнопками"""
        ws = sh.sheet1
        num = 1
        while True:
            if ws.cell(num, 2).value is not None:
                num += 1
            else:
                ws.update_cell(num, 2, str(check))
                break
        bot.send_message(
            message.chat.id,
            'Дата верна',
            reply_markup=gen_markup(bot)
        )
        bot.delete_state(message.from_user.id)
    except ValueError:
        """Если дата введена неверно, вызываем исключение и отправляем сообщение об ошибке ввода"""
        bot.send_message(
            message.chat.id,
            'Дата введена неверно.\nПопробуйте еще раз в формате: ГГГГ-ММ-ДД'
        )
        return
