from datetime import datetime

import telebot
from telebot import types

from DataBaseClass import DataBase

BOT_TOKEN = '6687303614:AAE6oFosY9JKmCRcJYY4zg1kh3Gud9o2U_A'
bot = telebot.TeleBot(token=BOT_TOKEN)

DATA = {
    'title': None,
    'text': None,
    'photos': None,
    'region': None,
    'user': None,
    'date': None,
    'coordinates': None,
}

STATUS_TEXT: str = 'Узнать статус проблем'
NEW_PROBLEM_TEXT: str = 'Объявить о новой проблеме'
DATABASE = DataBase()


@bot.message_handler(commands=['start'])
def start_message(message):
    """Функиця срабатывает при старте бота."""
    message_to_chat = (
        'Привет, я Эко-Бот!\nТы можешь сообщить'
        ' о проблеме связанной с мусором на побережьях'
        ' и мы решим ее.\nПеред использованием убедитесь, что'
        ' ваш номер телефона зарегистрирован на нашем сайте!'
        ' Напишите свой номер телефона.'
    )
    bot.send_message(message.chat.id, message_to_chat)
    bot.register_next_step_handler(message, contact_handler)


@bot.message_handler(func=lambda message: True)
def contact_handler(message):
    if DATABASE.auth(message.text):
        message_to_chat = 'Вы аутентифицировались!'
        bot.send_message(message.chat.id, message_to_chat)
        markup = types.ReplyKeyboardMarkup()
        status = types.KeyboardButton(STATUS_TEXT)
        new_problem = types.KeyboardButton(NEW_PROBLEM_TEXT)
        markup.row(status, new_problem)
        bot.send_message(message.chat.id, message_to_chat, reply_markup=markup)
        bot.register_next_step_handler(message, on_click)
    else:
        message_to_chat = (
            'Вашего номера нет в базе данных.'
            ' Вам необходимо пройти регистрацию на нашем сайте.'
        )
        bot.send_message(message.chat.id, message_to_chat)


@bot.message_handler(func=lambda message: True)
def on_click(message):
    """
    Функция срабатывает при выборе кнопок:
    узнать о статусе и объявить о проблеме
    """
    if message.text == STATUS_TEXT:
        message_to_chat = 'Эта функция еще не реализована!'
        bot.send_message(message.chat.id, message_to_chat)
    else:
        message_to_chat = 'Укажите заголовок проблемы'
        bot.send_message(message.chat.id, message_to_chat)
        bot.register_next_step_handler(message, after_title)


@bot.message_handler(func=lambda message: True)
def after_title(message):
    DATA['title'] = message.text
    DATA['date'] = datetime.now()
    message_to_chat = 'Укажите текст проблемы'
    bot.send_message(message.chat.id, message_to_chat)
    bot.register_next_step_handler(message, after_text)


@bot.message_handler(func=lambda message: True)
def after_text(message):
    DATA['text'] = message.text
    message_to_chat = ''


bot.infinity_polling()
