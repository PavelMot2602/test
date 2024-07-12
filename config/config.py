import os
from dotenv import load_dotenv, find_dotenv
from gspread import Client, Spreadsheet
import gspread


if not find_dotenv():
    """Проверяем есть ли токен бота в виртуальном окружении"""
    exit('Переменные окружения не загружены, так как отсутствует файл .env')
else:
    load_dotenv()

"""Создаем переменные для запуска и полноценной работы бота"""
BOT_TOKEN = os.getenv('BOT_TOKEN')
SCOPE = 'https://docs.google.com/spreadsheets/d/1ZBsrsNNbkmZC-JbGxgPr2hfcqczq2_Mc3bTT2oOsw-s/edit?gid=0#gid=0'
gc: Client = gspread.service_account('./bot1.json')
sh: Spreadsheet = gc.open_by_url(SCOPE)
DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('maps', 'Посмотреть адрес'),
    ('pay', 'Получить ссылку на оплату'),
    ('image', 'Получить картинку'),
    ('table', 'Получить значение из таблицы'),
    ('date', 'Ввести дату')
)
