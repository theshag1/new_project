import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(
    dbname='wtu',
    user='postgres',
    password='12345',
    host='localhost',
    port=5432

)
cur = connection.cursor(cursor_factory=RealDictCursor)
sql = "insert into staff(first_name, last_name, regoin, phone) values (%s, %s, %s, %s)"
cur.execute(sql, ("luda", 'jon', 't', '999197'))
connection.commit()
print(cur)