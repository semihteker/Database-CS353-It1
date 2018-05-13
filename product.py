import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'Mantı', 'Pastas', 21, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'FitKahvalti', 'Breakfast,' 14, 200 )")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'Menemen', 'Breakfast', 21, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'Tavuklu Wrap', 'MainDish', 19, 270)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'Kofte', 'MainDish', 21, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'Brownie', 'Desserts', 14, 200 )")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'Fettuccine', 'Pastas', 21, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'Pancake', 'Desserts', 16, 270)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'Latte' , 'Drinks', 12, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (1, 'NaneliAyran', 'Drinks', 16 200 )")

cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'Tuzlama', 'Soup', 16, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'Mercimek', 'Soup', 7, 200 )")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'IzgaraSucuk', 'BBQ', 24, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'MidyeTava', 'BBQ', 16, 270)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'IslakHamburger', 'Hamburgers', 5, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'Hamburger', 'Hamburger', 10, 200 )")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'Trilece', 'Desserts', 7, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'Kokorec', 'MainDish', 16, 270)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'Salgam' , 'Drinks', 3, 150)")
cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
            VALUES (2, 'Pepsi', 'Drinks', 4, 200 )")

conn.commit()
conn.close()
