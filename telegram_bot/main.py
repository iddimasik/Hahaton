import base64
import io
from datetime import datetime
from PIL import Image

import telebot
from telebot import types

from DataBaseClass import DataBase


BOT_TOKEN = '6687303614:AAE6oFosY9JKmCRcJYY4zg1kh3Gud9o2U_A'
bot = telebot.TeleBot(token=BOT_TOKEN)

authenticated = {}

# Словарь, в котором формируются данные для создания записи.
DATA = {

}

STATUS_TEXT: str = 'Узнать статус проблем'
NEW_PROBLEM_TEXT: str = 'Объявить о новой проблеме'

# Объект базы данных.
DATABASE = DataBase()


@bot.message_handler(commands=['start'])
def start_message(message):
    """Функиця срабатывает при старте бота."""
    message_to_chat = (
        'Привет👋, я Эко-Бот🤖!\n\nВы можете сообщить'
        ' о проблеме связанной с мусором на побережьях🚯'
        ' и мы решим ее🧹.\n\nПеред использованием убедитесь, что'
        ' ваш номер телефона зарегистрирован на нашем сайте📱🤩!\n\n'
        ' Напишите свой номер телефона.'
    )
    bot.send_message(message.chat.id, message_to_chat)
    bot.register_next_step_handler(message, auth_user)


def auth_user(message):
    """Фунция-проверка номера телефона в БД."""
    markup = types.ReplyKeyboardMarkup()
    status_button = types.KeyboardButton(STATUS_TEXT)
    new_problem_button = types.KeyboardButton(NEW_PROBLEM_TEXT)
    markup.row(status_button, new_problem_button)
    print(message.chat.id)

    if message.chat.id in authenticated:
        bot.send_message(
            message.chat.id,
            'Выберете действие:',
            reply_markup=markup
        )
        print(authenticated)
        bot.register_next_step_handler(message, choice)
    else:
        phone_number = message.text
        user_id = DATABASE.auth(phone_number)
        if user_id:
            authenticated[message.chat.id] = user_id
            DATA[message.chat.id] = {}
            DATA[message.chat.id]['user_id'] = authenticated[message.chat.id]
            bot.send_message(
                message.chat.id,
                'Авторизация прошла успешно!🤩\n'
                'Теперь вы можете:\n\nПросмотреть статусы☁'
                ' выполнения проблемы или объявить о новой проблеме🤔.',
                reply_markup=markup
            )
            bot.register_next_step_handler(message, choice)
        else:
            bot.send_message(
                message.chat.id,
                'Такого номера нет в нашей базе данных😭!\n'
                'Попробуйте снова ввести номер телефона📱.'
            )
            bot.register_next_step_handler(message, auth_user)


def choice(message):
    """Функция обработки выбора пользователя."""
    user_choice = message.text
    keyboard_remove = types.ReplyKeyboardRemove()
    if user_choice == STATUS_TEXT:
        # Получение данных по id пользователя
        bot.send_message(
            message.chat.id,
            'Высылаю вам статусы проблем,'
            ' которые были отправлены вами☁🤔...',
        )
        user_problems = DATABASE.get_problem_dict(DATA[message.chat.id]['user_id'])
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
        # Точка отправки на создание записи.
        bot.send_message(
            message.chat.id,
            'Введите заголовок проблемы🤔:',
            reply_markup=keyboard_remove
        )
        bot.register_next_step_handler(message, get_title)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка: то значение,'
            ' которое вы выбрали - не существует🤔😭!\n'
            'Попробуйте снова.'
        )
        bot.register_next_step_handler(message, choice)


def get_title(message):
    """Функция для получения заголовка проблемы."""
    title = message.text
    if title:
        DATA[message.chat.id]['problem_title'] = title
        bot.send_message(
            message.chat.id,
            f'Спасибо, я сохранил ваш заголовок'
            f' - {title}. Введите текст проблемы🗣:'
        )
        bot.register_next_step_handler(message, get_text)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка❗❗❗\nВозможно вы'
            ' отправили пустую строку. Введите еще раз.'
        )
        bot.register_next_step_handler(message, get_title)


def get_text(message):
    """Функция для получения текста проблемы."""
    text = message.text
    if text:
        DATA[message.chat.id]['problem_text'] = text
        DATA[message.chat.id]['problem_status'] = 'На рассмотрении'
        bot.send_message(
            message.chat.id,
            'Текст проблемы сохранен👍.\n\nОтправьте фотографию📸,'
            ' чтобы оценить масштабы загрязнения🚯.'
        )
        bot.register_next_step_handler(message, get_photos)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка❗❗❗\nПопробуйте ввести текст снова.'
        )
        bot.register_next_step_handler(message, get_text)


def get_photos(message):
    """Функция для получения фотографии проблемы."""
    if message.photo and not isinstance(message.photo, str):
        for photo in message.photo:
            file_id = photo.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            file_bytes = bot.download_file(file_path)
            image = Image.open(io.BytesIO(file_bytes))
            if image.format == 'JPEG':
                print('JPEG')
            if image.format == 'JPG':
                print('JPG')
            if image.format == 'PNG':
                print('PNG')
            encoded_image = str(base64.b64encode(file_bytes))
            DATA[message.chat.id]['image_data'] = encoded_image[2:len(encoded_image) - 1]
        regions = DATABASE.get_regions()
        markup = types.ReplyKeyboardMarkup(row_width=1)
        for region_id, region_name in regions:
            region_button = types.KeyboardButton(region_name)
            markup.add(region_button)
        bot.send_message(
            message.chat.id,
            'Ваша фотография была успешно сохранена👍.\n\n'
            'Укажите регион, в котором находится проблема:',
            reply_markup=markup
        )
        bot.register_next_step_handler(message, get_region)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка❗❗❗\nВы ваши данные'
            ' не являются фотографией. Попробуйте снова.'
        )
        bot.register_next_step_handler(message, get_photos)


def get_region(message):
    """Функция для получения региона проблемы."""
    user_region = message.text
    regions = DATABASE.get_regions()
    region_index = None

    for region_id, region_name in regions:
        if user_region == region_name:
            region_index = region_id

    if region_index is not None:
        DATA[message.chat.id]['region_id'] = region_index
        keyboard_remove = types.ReplyKeyboardRemove()
        bot.send_message(
            message.chat.id,
            'Регион, в котором находиться'
            ' проблема, был успешно сохранен. Пришлите точную'
            ' геопозицию, где находится проблема🗺.\n\n'
            'ПРИМЕЧАНИЕ: Если вы используете нашего чат-бота на'
            ' компьютре, то воспользуйтесь'
            ' https://yandex.ru/maps/?ll=39.944896%2C46.825533&z=9.47'
            ' и отправьте координаты места в чат.',
            reply_markup=keyboard_remove
        )
        bot.register_next_step_handler(message, get_location)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка❗❗❗\nТакого региона нет'
            ' в базе данных. Попробуйте еще раз:'
        )
        bot.register_next_step_handler(message, get_region)


def check_coords(coords):
    flag = True
    try:
        coords = coords.replace(' ', '')
        coords = coords.split(',')
        if len(coords) != 2:
            flag = False
        coords = [float(element) for element in coords]
    except ValueError:
        flag = False
    return flag


def get_location(message):
    """Функция для получения геолокации проблемы."""
    markup = types.ReplyKeyboardMarkup()
    success_button = types.KeyboardButton('Готово')
    markup.add(success_button)

    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        DATA[message.chat.id]['coordinates_xy'] = f'{latitude} {longitude}'

        bot.send_message(
            message.chat.id,
            'Геопозиция была успешно сохранена👍!\n\n'
            'Ваш запрос был направлен на рассмотренией администрацией🤖.',
            reply_markup=markup
        )
        DATA[message.chat.id]['creation_date'] = datetime.now()

        # Вызов метода для записи полученных данных в БД.
        DATABASE.insert_data_in_db(DATA[message.chat.id])
        bot.register_next_step_handler(message, auth_user)
    elif isinstance(message.text, str):
        coordinates = message.text
        flag = check_coords(coordinates)

        if flag:
            coordinates = coordinates.replace(' ', '')
            coordinates = coordinates.split(',')
            DATA[message.chat.id]['coordinates_xy'] = str(float(coordinates[0])) + ' ' + str(float(coordinates[1]))
            bot.send_message(
                message.chat.id,
                'Геопозиция была успешно сохранена👍!\n\n'
                'Ваш запрос был направлен на рассмотренией администрацией🤖.',
                reply_markup=markup
            )
            DATA[message.chat.id]['creation_date'] = datetime.now()

            # Вызов метода для записи полученных данных в БД.
            DATABASE.insert_data_in_db(DATA[message.chat.id])
            bot.register_next_step_handler(message, auth_user)
        else:
            bot.send_message(
                message.chat.id,
                'Введенные вами данные некорректны❗❗❗\n'
                'Возможно вы не указали координаты через запятую.'
            )
            bot.register_next_step_handler(message, get_location)
    else:
        bot.send_message(
            message.chat.id,
            'Произошла ошибка❗❗❗\nВы прислали'
            ' неправильную геопозицию. Попробуйте еще раз'
        )
        bot.register_next_step_handler(message, get_location)


bot.infinity_polling()
