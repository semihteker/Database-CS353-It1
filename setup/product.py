import sqlite3

def xyz8():

    conn = sqlite3.connect('setup/database.db')
    cursor = conn.cursor()


    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (1, 'Manti', 'Pastas', 21, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (1, 'FitKahvalti', 'Breakfast', 14, 200 )")
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
                VALUES (1, 'NaneliAyran', 'Drinks', 16, 200 )")

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

    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'KingBurger', 'Burgers', 11, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'CheeseBurger', 'Burgers', 10, 200 )")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'FishFingers', 'Sneak',8 , 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'Nuggets', 'Sneak', 9, 270)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'DoubleBurger', 'Burgers', 14, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'DoubleChicken', 'Burgers', 12, 200 )")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'Coffee', 'Drinks', 6, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'Milkshake', 'IceCream', 5, 270)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'IceTea' , 'Drinks', 8, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (3, 'Sundae', 'IceCream', 4, 200 )")

    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'Karakoy', 'Kahvalti', 11, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'Form', 'Kahvalti', 24, 200 )")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'PastirmaYumurta', 'Sahanda', 24, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'PatatesYumurta', 'Sahanda', 16, 270)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'KarisikOmlet', 'Yumurta', 5, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'KasarliOmlet', 'Yumurta', 10, 200 )")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'Profiterol', 'Desserts', 12, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'KestaneliPasta', 'Desserts', 9, 270)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'Limonata' , 'Drinks', 12, 150)")
    cursor.execute("INSERT INTO product (rest_id, food_name, food_type, price, portion)\
                VALUES (4, 'Havuc', 'Drinks', 9, 200 )")

    conn.commit()
    conn.close()
