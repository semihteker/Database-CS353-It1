import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()




cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (1, 'home', 'Cayyolu', 5, 'Ankara', 06554, 'Mesa')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (1, 'school', 'BilkentUni', 8, 'Ankara', 06000, '74thdormitory')")

cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (2, 'home', 'Yenimahalle', 3, 'Ankara', 07554, 'Toki')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (2, 'school', 'BilkentUni', 8, 'Ankara', 06000, EABuilding)")


cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (3, 'home', 'Incek', 5, 'Ankara', 06554, 'Residences')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (3, 'school', 'BilkentUni', 8, 'Ankara', 06000, 'ABuilding')")


cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (4, 'home', 'Umitkoy', 5, 'Ankara', 06876, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (4, 'school', 'BilkentUni', 8, 'Ankara', 06000, 'BBuilding')")

cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (5, 'home', 5389467543, 'Maslak', 2, 'Istanbul2, 34076, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (5, 'work', 5389467543, 'KapaliCarsi',8, 'Istanbul', 34777, 'Carsi')")


cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (6, 'home', 'Bebek', 11, 'Istanbul', 34876, 'Home')")
ccursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (6, 'training', 'Florya', 2, 'Istanbul', 34854, 'GalatasarayTrainingPlace')")

cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (7, 'home',  'Fulya', 7, 'Istanbul', 34336, 'Apartment')")
ccursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (7, 'stadium',  'Besiktas', 8, 'Istanbul', 34974, 'BesiktasStadium')")


cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (8, 'home', 'Tarabya', 22, 'Istanbul', 34393, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (8, 'training',  'Umraniye', 211, 'Istanbul', 34974, 'BesiktasTraining')")

cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (9, 'home',  'Kadikoy', 17, 'Istanbul', 34982, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (9, 'training',  'Umraniye', 92, 'Istanbul', 34875, 'BesiktasTraining')")


cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (10, 'home', 'Yenikoy', 17, 'Istanbul', 34779, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc)\
            VALUES (10, 'training',  'Besiktas', 29, 'Istanbul', 34974, 'BesiktasStadium')")






conn.commit()
conn.close()
