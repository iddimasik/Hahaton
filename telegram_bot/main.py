from datetime import datetime

import base64
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
    'user_id': None,
    'date': None,
    'coordinates': None,
}

STATUS_TEXT: str = 'Узнать статус проблем'
NEW_PROBLEM_TEXT: str = 'Объявить о новой проблеме'
DATABASE = DataBase()


def output_files(message):
    print(DATA)
    bot.register_next_step_handler(message, contact_handler)


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
    user_id = DATABASE.auth(message.text)
    if user_id:
        message_to_chat = 'Вы аутентифицировались!'
        DATA['user_id'] = user_id
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
            ' После повторно напишите свой номер телефона.'
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
        keyboard_remove = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, message_to_chat, reply_markup=keyboard_remove)
        bot.register_next_step_handler(message, text_problem)


@bot.message_handler(func=lambda message: True)
def text_problem(message):
    DATA['title'] = message.text
    DATA['date'] = datetime.now()
    message_to_chat = 'Укажите текст проблемы'
    bot.send_message(message.chat.id, message_to_chat)
    bot.register_next_step_handler(message, get_text)


@bot.message_handler(func=lambda message: True)
def get_text(message):
    DATA['text'] = message.text
    bot.register_next_step_handler(message, photos_problem)


@bot.message_handler(func=lambda message: True)
def photos_problem(message):
    message_to_chat = 'Отправьте фотографии проблемы'
    bot.send_message(message.chat.id, message_to_chat)
    if message.photo:
        for photo in message.photo:
            file_id = photo.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            file_bytes = bot.download_file(file_path)
            byte_array = base64.b64encode(file_bytes)
            DATA['photos'] = str(byte_array)
            print(byte_array)
    bot.register_next_step_handler(message, regions)


@bot.message_handler(commands=['region'])
def regions(message):
    regions = DATABASE.get_regions()
    markup = types.ReplyKeyboardMarkup(row_width=1)
    message_to_chat = 'Выберите регион'
    for region_id, region_name in regions:
        button = types.KeyboardButton(region_name)
        markup.add(button)
    bot.send_message(message.chat.id, message_to_chat, reply_markup=markup)
    bot.register_next_step_handler(message, region)


@bot.message_handler(func=lambda message: True)
def region(message):
    regions = DATABASE.get_regions()
    region_index = None
    for region_id, region_name in regions:
        if message.text == region_name:
            region_index = region_id
    if region_index is None:
        bot.message_handler(
            message.chat.id,
            'Данного региона нет в нашей базе данных'
        )
        bot.register_next_step_handler(message, regions)
    DATA['region'] = region_index
    keyboard_remove = types.ReplyKeyboardRemove()
    bot.send_message(
        message.chat.id,
        'Отправьте геопозицию проблемы',
        reply_markup=keyboard_remove
    )
    bot.register_next_step_handler(message, location)


@bot.message_handler(commands=['location'])
def location(message):
    message_to_chat = (
        'Все данные приняты!'
        ' Чтобы дальше взаимодействовать с ботом введите номер телефона:'
    )
    if not message.location:
        bot.send_message(
            message.chat.id,
            'Ошибка: Вы не скинули геопозицию'
        )
        bot.register_next_step_handler(message, location)

    latitude = message.location.latitude
    longitude = message.location.longitude
    coords = f'{latitude}, {longitude}'
    DATA['coordinates'] = coords
    bot.send_message(message.chat.id, message_to_chat)
    output_files(message)


bot.infinity_polling()
