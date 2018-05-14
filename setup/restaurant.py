import sqlite3

def xyz9():

    conn = sqlite3.connect('setup/database.db')
    cursor = conn.cursor()


    cursor.execute("INSERT INTO restaurant (email, password, name, address, working_hours, isOpen, rate, d_id)\
                VALUES ('fameo@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Fameo', 'Istanbul', 10,1,4,2);")
    cursor.execute("INSERT INTO restaurant (email, password, name, address,  working_hours, isOpen, rate, d_id)\
                VALUES ('Sampiyon@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'SampiyonKokorec',' Ankara',  12, 1, 5, 3);")
    cursor.execute("INSERT INTO restaurant (email, password, name, address, working_hours, isOpen, rate, d_id)\
                VALUES ('burgerking@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'BurgerKing', 'Ankara', 20,11,24,22);")
    cursor.execute("INSERT INTO restaurant (email, password, name, address,  working_hours, isOpen, rate, d_id)\
                VALUES ('dubledoner@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'DubleDoner',' Istanbul',  112,21, 15, 23);")

    conn.commit()
    conn.close()
