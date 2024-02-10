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
                print('[DEBUG] Подключение прошло успешно.')
                cursor.execute(
                    """SELECT * FROM users;"""
                )
                users_data = cursor.fetchall()
                all_users = {}
                user_data = {
                    'id': None,
                    'name': None,
                    'last_name': None,
                    'email': None,
                    'user_status': None,
                    'role': None,
                    'phone_number': None,
                    'login': None,
                    'password': None
                }
                for user in users_data:
                    for user_value in user:
                        for key, value in user_data.items():
                            user_data[key] = user_value
                    all_users[user[0]] = user_data
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
                flag = True
                return True
        return False
