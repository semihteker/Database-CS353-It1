import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('semihteker14@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Semih', 'Teker', 5334447744)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('bahadirdurmaz11@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Bahadir', 'Durmaz', 5325554433)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('halilibrahimcavdar@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Halil',' Cavdar', 5347656554)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('berkaybeken@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Berkay', 'Beken', 5366544567)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('arifisik@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Arif', 'Isik', 5389467543)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('bafetimbigomis@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Bafetimbi', 'Gomis', 5334447744)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('senolgunes@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Senol', 'Gunes', 5543797044)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('oguzhanozyakup@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Oguzhan', 'Ozyakup', 5366799765)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('gokhangonul@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Gokhan', 'Gonul', 5343456546)")
cursor.execute("INSERT INTO customer (e_mail, password, name, surname, phone_number)\
            VALUES ('andersontalisca@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Anderson', 'Talisca', 5325838888")


conn.commit()
conn.close()
