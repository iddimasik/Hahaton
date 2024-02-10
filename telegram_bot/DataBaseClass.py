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
                print('[DEBUG] Подключение прошло успешно. Точка входа - таблица Users')
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
                    all_users[str(i + 1)] = data_dict
                return all_users

        except Exception as error:
            raise Exception(f'[CRITICAL] Что-то не так с подключением к базе данных - {error}!')
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
                print('[DEBUG] Подключение прошло успешно. Точка входа - таблица Regions')
                cursor.execute(
                    """SELECT * FROM regions;"""
                )
                all_regions = cursor.fetchall()
                return all_regions

        except Exception as error:
            raise Exception(f'[CRITICAL] Что-то не так с подключением к базе данных - {error}!')
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

            with connection.cursor() as cursor:
                print('[DEBUG] Подключение к базе данных прошло успешно. Точка входа - таблица')


        except Exception as error:
            raise Exception(f'[CRITICAL] Что-то не так с подключением к базе данных - {error}!')
        finally:
            if connection:
                connection.close()
                print('[DEBUG] Подключение успешно закрылось.')


element = DataBase()
print(element.auth('124'))
