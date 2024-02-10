import psycopg2
from pprint import pprint

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

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id
            FROM pollution_places
            WHERE coordinates_xy = '47.271604 39.776809';
            """
        )
        print('successfully get')
        pprint(cursor.fetchall()[0][0])


except Exception as error:
    print(f'Что-то не так с подключением - {error}')

finally:
    if connection:
        cursor.close()
        print('Запросы завершились')
