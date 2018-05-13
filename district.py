import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Yenimahalle', 'Ankara' )")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Bilkent', 'Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Cayyolu','Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Eryaman','Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Sincan','Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Kizilay', 'Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Ulus', 'Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Umitkoy', 'Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Yenimahalle', 'Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Kartal', 'Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Bakirkoy','Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Yasamkent','Ankara')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Bebek','Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Buyukcekmece','Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Taksim','Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Kadikoy','Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Besiktas','Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Levent','Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Maslak','Istanbul')")
cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Beyoglu','Istanbul')")


conn.commit()
conn.close()
