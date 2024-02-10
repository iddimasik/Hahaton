import psycopg2
from pprint import pprint

from config import db_name, host, password, user


class DataBase:

    def __init__(self):
        self.user = user
        self.password = password
        self.host = host
        self.db_name = db_name

    def get_users(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                print(
                    '[DEBUG] Подключение прошло успешно.'
                    ' Точка входа - таблица Users'
                )
                cursor.execute(
                    """SELECT * FROM users;"""
                )
                users_data = cursor.fetchall()
                keys = [
                    'id', 'first_name', 'last_name',
                    'email', 'user_status', 'role',
                    'phone_number', 'login', 'password'
                ]
                all_users = {}
                for i in range(len(users_data)):
                    data_dict = dict(zip(keys, users_data[i]))
                    all_users[i + 1] = data_dict
                return all_users

        except Exception as error:
            raise Exception(
                f'[CRITICAL] Что-то не так с '
                f'подключением к базе данных - {error}!'
            )
        finally:
            if connection:
                connection.close()
                print('[DEBUG] Подключение успешно закрылось.')

    def auth(self, phone_number_from_telegram):
        all_users = self.get_users()
        flag = False
        for data_user in all_users.values():
            if data_user['phone_number'] == phone_number_from_telegram:
                return data_user['id']
        return flag

    def get_regions(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            connection.autocommit = True

            with connection.cursor() as cursor:
                print(
                    '[DEBUG] Подключение прошло успешно. '
                    'Точка входа - таблица Regions'
                )
                cursor.execute(
                    """SELECT * FROM regions;"""
                )
                all_regions = cursor.fetchall()
                return all_regions

        except Exception as error:
            raise Exception(
                f'[CRITICAL] Что-то не так с'
                f' подключением к базе данных - {error}!'
            )
        finally:
            if connection:
                connection.close()
                print('[DEBUG] Подключение успешно закрылось.')

    def insert_data_in_db(self, data):
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            connection.autocommit = True

            image_data = {}
            image_data['image_data'] = data.pop('image_data')
            date = {}
            date['creation_date'] = data['creation_date']
            data_query_insert_problem = """
            INSERT INTO pollution_places (
            problem_title, problem_text,  problem_status,
            region_id, user_id, creation_date, coordinates_xy
            )
            VALUES (
            %(problem_title)s, %(problem_text)s, %(problem_status)s,
            %(region_id)s, %(user_id)s, %(creation_date)s, %(coordinates_xy)s);
            """
            data_query_get_id = """
            SELECT id
            FROM pollution_places
            WHERE creation_date = %(creation_date)s;
            """
            data_query_insert_photo = """
            INSERT INTO images (image_data, pollution_place_id)
            VALUES (%(image_data)s, %(pollution_place_id)s);
            """

            with connection.cursor() as cursor:
                print(
                    '[DEBUG] Подключение к базе данных прошло'
                    ' успешно. Точка входа - таблица Pollution_Places.'
                )
                cursor.execute(data_query_insert_problem, data)
                print(
                    '[DEBUG] Данные полученные из телеграм'
                    ' бота успешно создали новую запись [ПРОБЛЕМА].'
                )
                cursor.execute(data_query_get_id, date)
                image_data['pollution_place_id'] = cursor.fetchall()[0][0]
                print(
                    '[DEBUG] Из таблицы Pollution_Places'
                    ' был получен id из созданной записи'
                )
                cursor.execute(data_query_insert_photo, image_data)
                print(
                    '[DEBUG] Данные полученные из телеграм'
                    ' бота успешно создали новую запись [ФОТО].'
                )
        except Exception as error:
            raise Exception(
                f'[CRITICAL] Что-то не так с '
                f'подключением к базе данных - {error}!'
            )
        finally:
            if connection:
                connection.close()
                print('[DEBUG] Подключение успешно закрылось.')
