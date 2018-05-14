import sqlite3

def xyz6():

    conn = sqlite3.connect('setup/database.db')
    cursor = conn.cursor()


    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('semihteker14@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Semih', 'Teker' )")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('bahadirdurmaz11@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Bahadir', 'Durmaz')")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('halilibrahimcavdar@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Halil',' Cavdar')")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('berkaybeken@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Berkay', 'Beken')")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('arifisik@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Arif', 'Isik')")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('bafetimbigomis@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Bafetimbi', 'Gomis')")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('senolgunes@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Senol', 'Gunes')")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('oguzhanozyakup@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Oguzhan', 'Ozyakup')")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('gokhangonul@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Gokhan', 'Gonul')")
    cursor.execute("INSERT INTO customer (email, password, name, surname)\
                VALUES ('andersontalisca@gmail.com', 'pbkdf2:sha256:50000$IJWtrzho$307e9da66701e2e88474e8e7b55eff103b7ca8c051c56c2b7c69f9646067ca4e', 'Anderson', 'Talisca')")


    conn.commit()
    conn.close()
