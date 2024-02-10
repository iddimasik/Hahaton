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
            SELECT problem_title, problem_status, creation_date, coordinates_xy
            FROM pollution_places
            WHERE user_id = '1';
            """
        )
        print('successfully get')
        pprint(cursor.fetchall())


except Exception as error:
    print(f'Что-то не так с подключением - {error}')

finally:
    if connection:
        cursor.close()
        print('Запросы завершились')
