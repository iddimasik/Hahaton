import psycopg2

from config import db_name, host, password, user

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            'Select version();'
        )
        print(f'Server version {cursor.fetchone()}')
    users = []
    with connection.cursor() as cursor:
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
        print(all_users)


except Exception as error:
    print(f'Что-то не так с подключением - {error}')

finally:
    if connection:
        cursor.close()
        print('Запросы завершились')
