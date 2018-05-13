import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO district (district_name,city)\
            VALUES ('Yenimahalle','Ankara');")

cursor.execute("INSERT INTO restaurant (email,password,name,address,working_hours,isOpen,rate,d_id) \
            VALUES ('rest@home.com','pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e',\
                'sözeri','alt sokak', '9-15', 1, 8.4, 5);")

conn.commit()
conn.close()
