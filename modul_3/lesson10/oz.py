import psycopg2

connection = psycopg2.connect(
    dbname='trellobot',
    user='postgres',
    password='12345',
    host='localhost',
    port=5432
)
