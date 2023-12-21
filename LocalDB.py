import psycopg2
from psycopg2 import sql
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname='имя_базы_данных',
    user='имя_пользователя',
    password='ваш_пароль',
    host='адрес_хоста',
    port='порт'
)

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# Путь к CSV-файлу
csv_file_path = '/путь/к/вашему_файлу.csv'

# Название таблицы, в которую вы хотите загрузить данные
table_name = 'название_вашей_таблицы'

# SQL-запрос для создания временной таблицы для загрузки данных из CSV
create_table_query = f'''
    CREATE TEMP TABLE temp_table
    (/* перечислите столбцы вашей таблицы и их типы здесь */);
'''

# Используйте try-except для обработки исключений
try:
    # Создание временной таблицы
    cur.execute(create_table_query)

    # Чтение данных из CSV файла и загрузка их во временную таблицу
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Пропуск заголовка, если он есть
        for row in reader:
            # SQL-запрос для вставки данных во временную таблицу
            insert_query = sql.SQL('INSERT INTO {} VALUES {}').format(
                sql.Identifier('temp_table'),
                sql.Literal(tuple(row))
            )
            cur.execute(insert_query)

    # Коммит изменений
    conn.commit()

    # Копирование данных из временной таблицы в вашу основную таблицу
    copy_query = f'''
        INSERT INTO {table_name}
        SELECT * FROM temp_table;
    '''
    cur.execute(copy_query)

    # Коммит изменений
    conn.commit()

except psycopg2.Error as e:
    print("Ошибка при работе с PostgreSQL:", e)
finally:
    # Закрытие курсора и соединения
    cur.close()
    conn.close()