from datetime import datetime

import base64
import telebot
from telebot import types

from DataBaseClass import DataBase


BOT_TOKEN = '6687303614:AAE6oFosY9JKmCRcJYY4zg1kh3Gud9o2U_A'
bot = telebot.TeleBot(token=BOT_TOKEN)

DATA = {
    'problem_title': None,
    'problem_text': None,
    'problem_status': 'На рассмотрении',
    'region_id': None,
    'user_id': None,
    'creation_date': None,
    'coordinates_xy': None,
    'image_data': None,
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
    bot.register_next_step_handler(message, auth_user)


def auth_user(message):
    markup = types.ReplyKeyboardMarkup()
    status_button = types.KeyboardButton(STATUS_TEXT)
    new_problem_button = types.KeyboardButton(NEW_PROBLEM_TEXT)
    markup.row(status_button, new_problem_button)

    if DATA['user_id'] is not None:
        bot.send_message(
            message.chat.id,
            'Выберете действие:',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, choice)
    else:
        phone_number = message.text
        user_id = DATABASE.auth(phone_number)
        if user_id:
            DATA['user_id'] = user_id
            bot.send_message(
                message.chat.id,
                'Авторизация прошла успешно!'
                ' Теперь вы можете: Просмотреть статусы'
                ' выполнения проблемы или объявить о новой проблеме.',
                reply_markup=markup
            )
            bot.register_next_step_handler(message, choice)
        else:
            bot.send_message(
                message.chat.id,
                'Такого номера нет в нашей базе данных!'
                ' Попробуйте снова ввести номер телефона.'
            )
            bot.register_next_step_handler(message, auth_user)


def choice(message):
    user_choice = message.text
    keyboard_remove = types.ReplyKeyboardRemove()
    if user_choice == STATUS_TEXT:
        bot.send_message(
            message.chat.id,
            'Высылаю вам статусы проблем,'
            ' которые были отправлены вами...',
        )
        user_problems = DATABASE.get_problem_dict(DATA['user_id'])
        for problem_num, problem_dict in user_problems.items():
            message_to_chat = (
                f'{problem_num}) {problem_dict['problem_title']}\n'
                f'Статус: {problem_dict['problem_status']}\n'
                f'Координаты: {problem_dict['coordinates_xy']}\n'
                f'Дата создания: {problem_dict['creation_date']}'
            )
            markup = types.ReplyKeyboardMarkup()
            success_button = types.KeyboardButton('Готово')
            markup.add(success_button)
            bot.send_message(
                message.chat.id,
                message_to_chat,
                reply_markup=markup
            )
        bot.register_next_step_handler(message, auth_user)

    elif user_choice == NEW_PROBLEM_TEXT:
        bot.send_message(
            message.chat.id,
            'Введите заголовок проблемы:',
            reply_markup=keyboard_remove
        )
        bot.register_next_step_handler(message, get_title)
    else:
        bot.send_message(
            message.chat_id,
            'Произошла ошибка: то значение,'
            ' которое вы выбрали - не существует!'
            ' Попробуйте снова.'
        )
        bot.register_next_step_handler(message, choice)


def get_title(message):
    title = message.text
    if title:
        DATA['problem_title'] = title
        bot.send_message(
            message.chat.id,
            f'Спасибо, я сохранил ваш заголовок - {title}. Введите текст проблемы:'
        )
        bot.register_next_step_handler(message, get_text)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка, возможно вы отправили пустую строку. Введите еще раз'
        )
        bot.register_next_step_handler(message, get_title)


def get_text(message):
    text = message.text
    if text:
        DATA['problem_text'] = text
        bot.send_message(
            message.chat.id,
            'Текст проблемы сохранен. Отправьте фотографии,'
            ' чтобы оценить масштабы вашей проблемы.'
        )
        bot.register_next_step_handler(message, get_photos)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка. Попробуйте ввести текст снова.'
        )
        bot.register_next_step_handler(message, get_text)


def get_photos(message):
    if message.photo and not isinstance(message.photo, str):
        for photo in message.photo:
            file_id = photo.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            file_bytes = bot.download_file(file_path)
            encoded_image = str(base64.b64encode(file_bytes))
            DATA['image_data'] = encoded_image[2:len(encoded_image) - 1]
        regions = DATABASE.get_regions()
        markup = types.ReplyKeyboardMarkup(row_width=1)
        for region_id, region_name in regions:
            region_button = types.KeyboardButton(region_name)
            markup.add(region_button)
        bot.send_message(
            message.chat.id,
            'Ваши фотографии были успешно сохранены.'
            ' Укажите регион, в котором находится проблема:',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, get_region)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка: Вы ваши данные'
            ' не являются фотографией. Попробуйте снова.'
        )
        bot.register_next_step_handler(message, get_photos)


def get_region(message):
    user_region = message.text
    regions = DATABASE.get_regions()
    region_index = None

    for region_id, region_name in regions:
        if user_region == region_name:
            region_index = region_id

    if region_index is not None:
        DATA['region_id'] = region_index
        keyboard_remove = types.ReplyKeyboardRemove()
        bot.send_message(
            message.chat.id,
            'Регион, в котором находиться'
            ' проблема, был успешно сохранен. Пришлите точную'
            ' геопозицию, где находиться проблема',
            reply_markup=keyboard_remove
        )
        bot.register_next_step_handler(message, get_location)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка: такого региона нет'
            ' в базе данных. Попробуйте еще раз:'
        )
        bot.register_next_step_handler(message, get_region)


def get_location(message):
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        DATA['coordinates_xy'] = f'{latitude} {longitude}'
        markup = types.ReplyKeyboardMarkup()
        success_button = types.KeyboardButton('Готово')
        markup.add(success_button)
        bot.send_message(
            message.chat.id,
            'Геопозиция была успешно сохранена! '
            'Ваш запрос был направлен на рассмотренией администрацией.',
            reply_markup=markup
        )
        DATA['creation_date'] = datetime.now()
        DATABASE.insert_data_in_db(DATA)
        bot.register_next_step_handler(message, auth_user)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка: вы прислали'
            ' неправильную геопозицию. Попробуйте еще раз'
        )
        bot.register_next_step_handler(message, get_location)


bot.infinity_polling()
