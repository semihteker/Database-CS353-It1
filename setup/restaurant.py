import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO restaurant (email, password, name, address, working_hours, isOpen, rate, d_id)\
            VALUES ('fameo@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Fameo', 'Istanbul', 10,1,4,2);")
cursor.execute("INSERT INTO restaurant (email, password, name, address,  working_hours, isOpen, rate, d_id)\
            VALUES ('lokal71@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Lokal71',' Ankara',  12, 1, 5, 3);")

conn.commit()
conn.close()
