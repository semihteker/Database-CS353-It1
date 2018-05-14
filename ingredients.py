import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('yumurta', 90, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('domates', 70, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('biber', 60, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('kiyma', 120, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('hamur', 190, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('zeytin', 70, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('omlet', 220, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('tavukparca', 120, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('sogan', 70, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('brownie', 300, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('sugar', 70, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('coffee', 180, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('milk', 100, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('yoghurt', 86, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('mint', 20, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('tuzlama', 200, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('mercimek', 120, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('lemon', 50, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('karabiber', 10, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('sucuk', 200, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('bread', 190, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('midye', 170, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('potato', 220, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('burger', 320, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('oil', 90, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('salad', 50, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('trilece', 140, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('kokorec', 220, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('salgam', 90, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('coke', 200, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('cheese', 60, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('fish', 140, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('nugget', 160, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('banana', 120, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('IceTea', 190, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('Sundae', 170, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('borek', 220, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('egg', 90, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('pastirma', 80, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('sousage', 100, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('profiterol', 270, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('chocalate', 100, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('Maroni', 100, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('Water', 46, 1 )"
cursor.execute("INSERT INTO ingredient (ingr_name, ingr_calorie, quantity)\
            VALUES ('Carrot', 80, 1 )"

c

conn.commit()
conn.close()
