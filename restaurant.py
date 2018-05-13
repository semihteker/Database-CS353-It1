import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO product (e_mail, password, name, address, rest_phone, working hours, isOpen, rate, d_id)\
            VALUES ('fameo@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Fameo', 'Istanbul', 5332377844,10,'yes',4,d_id)")
cursor.execute("INSERT INTO restaurant (e_mail, password, name, surname, phone_number)\
            VALUES ('lokal71@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Lokal71',' Ankara', 5325554433, 12, 'yes', 5, d_id)")

conn.commit()
conn.close()
