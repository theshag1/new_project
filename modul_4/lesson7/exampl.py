import psycopg2

con = psycopg2.connect(
    dbname='wtu',
    user='postgres',
    password='12345',
    host='localhost',
    port=5432
)


cur = con.cursor()
cur.execute('select * from staff')
rows = cur.fetchall()
for row in rows:
    print(row[3])