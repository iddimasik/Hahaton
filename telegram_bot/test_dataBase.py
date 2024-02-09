import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'Select version();'
        )
        print(f'Server version {cursor.fetchone()}')

except Exception as error:
    print('Что-то не так с подключением')

finally:
    if connection:
        cursor.close()
        print('Запросы завершились')
