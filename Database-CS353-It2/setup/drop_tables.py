import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS customer;")
cursor.execute("select name from sqlite_master where type = 'table';")

tables = cursor.fetchall()


print(tables)
for table in tables:
    print(table)
    cursor.execute("DROP TABLE IF EXISTS %s;"%(table))
conn.commit()
conn.close()
