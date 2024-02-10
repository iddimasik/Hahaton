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
    'user_id': None,
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
    user_id = DATABASE.auth(message.text)
    if user_id:
        message_to_chat = 'Вы аутентифицировались!'
        DATA['user_id'] = user_id
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
        bot.send_message(message.chat.id, message_to_chat)
        bot.register_next_step_handler(message, text_problem)


@bot.message_handler(func=lambda message: True)
def text_problem(message):
    DATA['title'] = message.text
    DATA['date'] = datetime.now()
    message_to_chat = 'Укажите текст проблемы'
    bot.send_message(message.chat.id, message_to_chat)
    bot.register_next_step_handler(message, photos_problem)


@bot.message_handler(content_types=['photo'])
def photos_problem(message):
    DATA['text'] = message.text
    message_to_chat = 'Отправьте фотографии проблемы'
    bot.send_message(message.chat.id, message_to_chat)
    for photo in message.photo:
        file_id = photo.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        file_bytes = bot.download_file(file_path)
        byte_array = bytearray(file_bytes)
        with open('photo.txt', 'w') as file:
            file.write(str(byte_array))
        break
    bot.register_next_step_handler(message, regions)


@bot.message_handler(commands=['region'])
def regions(message):
    DATA['text'] = message.text
    regions = DATABASE.get_regions()
    markup = types.ReplyKeyboardMarkup(row_width=1)
    message_to_chat = 'Выберите регион'
    for region_id, region_name in regions:
        button = types.KeyboardButton(region_name)
        markup.add(button)
    bot.send_message(message.chat.id, message_to_chat, reply_markup=markup)
    bot.register_next_step_handler(message, location)


@bot.message_handler(func=lambda message: True)
def location(message):
    regions = DATABASE.get_regions()
    region_index = None
    for region_id, region_name in regions:
        if message.text == region_name:
            region_index = region_id
    DATA['region'] = region_index
    bot.send_message(
        message.chat.id,
        'Отправьте геопозицию проблемы'
    )
    bot.register_next_step_handler(message, location)


@bot.message_handler(commands=['location'])
def location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    coords = f'{latitude}, {longitude}'
    DATA['coordinates'] = coords


bot.infinity_polling()
