import sqlite3

def xyz3():

    conn = sqlite3.connect('setup/database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Manti', 'kiyma', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Manti', 'hamur', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'FitKahvalti', 'omlet', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'FitKahvalti', 'cheese', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'FitKahvalti', 'zeytin', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'FitKahvalti', 'domates', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Menemen', 'yumurta', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Menemen', 'domates', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'menemen', 'biber', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Tavuklu Wrap', 'tavuk', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Tavuklu Wrap', 'hamur', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Kofte', 'kiyma', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Kofte', 'sogan', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Brownie', 'brownie', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Brownie', 'sugar', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Fettuccine', 'hamur', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Pancake', 'yumurta', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Pancake', 'sugar', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Latte', 'coffee', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'Latte', 'milk', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'NaneliAyran', 'mint', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (1,'NaneliAyran', 'yoghurt', )"
                   
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Tuzlama', 'Tuzlama', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Tuzlama', 'water', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Mercimek', 'mercimek', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Mercimek', 'lemon', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Mercimek', 'karabiber', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'IzgaraSucuk', 'sucuk', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'IzgaraSucuk', 'bread', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'MidyeTava', 'midye', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'IslakHamburger', 'burger', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'IslakHamburger', 'bread', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Hamburger', 'onion', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Hamburger', 'burger', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Hamburger', 'bread', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Trilece', 'trilece', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Kokorec', 'kokorec', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Salgam', 'salgam', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (2,'Pepsi', 'coke', )"

                   
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'KingBurger', 'burger', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'KingBurger', 'salad', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'KingBurger', 'domates', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'KingBurger', 'bread', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'CheeseBurger', 'burger', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'CheeseBurger', 'salad', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'CheeseBurger', 'domates', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'CheeseBurger', 'bread', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'CheeseBurger', 'cheese', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'FishFingers', 'fish', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'Nuggets', 'nugget', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'DoubleBurger', 'salad', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'DoubleBurger', 'burger', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'DoubleBurger', 'domates', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'DoubleBurger', 'bread', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'DoubleChicken', 'chicken', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'DoubleChicken', 'salad', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'DoubleChicken', 'domates', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'DoubleChicken', 'bread', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'Coffee', 'coffee', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'Milkshake', 'milk', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'Milkshake', 'banana', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'IceTea', 'IceTea', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (3,'Sundae', 'Sandae', )"

                   
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Karakoy', 'borek', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Form', 'bread', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Form', 'zeytin', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Form', 'egg', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Form', 'domates', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Form', 'milk', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'PastirmaYumurta', 'egg', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'PastirmaYumurta', 'pastirma', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'PatatesYumurta', 'potato', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'PatatesYumurta', 'egg', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'KarisikOmlet', 'egg', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'KarisikOmlet', 'cheese', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'KarisikOmlet', 'sousage', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'KasarliOmlet', 'egg', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'KasarliOmlet', 'cheese', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Profiterol', 'profiterol', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Profiterol', 'chocalate', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'KestaneliPasta', 'Maroni', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'KestaneliPasta', 'Sugar', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Limonata', 'lemon', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Limonata', 'sugar', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Limonata', 'water', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'Havuc', 'carrot', )"
    cursor.execute("INSERT INTO constains (rest_id, food_name, ingr_name)\
                VALUES (4,'Havuc', 'Sugar', )"
    cursor.execute("INSERT INTO contains (rest_id, food_name, ingr_name)\
                VALUES (4,'PatatesYumurta', 'egg', )"

    conn.commit()
    conn.close()

