import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()




cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (1, 'home', 'Semih', 'Teker', 5334447744, 'Cayyolu', 5, 'Ankara', 06554, 'Mesa')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (1, 'school', 'Semih', 'Teker', 5334447744, 'BilkentUni', 8, 'Ankara', 06000, '74thdormitory')")

cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (2, 'home', 'Bahadir', 'Durmaz', 5342447744, 'Yenimahalle', 3, 'Ankara', 07554, 'Toki')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (2, 'school', 'Bahadir', 'Durmaz', 5342447744, 'BilkentUni', 8, 'Ankara', 06000, EABuilding)")


cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (3, 'home', 'Halil', 'Cavdar', 5347656554, 'Incek', 5, 'Ankara', 06554, 'Residences')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (3, 'school', 'Halil', 'Cavdar', 5347656554, 'BilkentUni', 8, 'Ankara', 06000, 'ABuilding')")


cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (4, 'home', 'Berkay', 'Beken', 5366544567, 'Umitkoy', 5, 'Ankara', 06876, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (4, 'school', 'Berkay', 'Beken', 5366544567, 'BilkentUni', 8, 'Ankara', 06000, 'BBuilding')")

cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (5, 'home', 'Arif', 'Isik', 5389467543, 'Maslak', 2, 'Istanbul2, 34076, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (5, 'work', 'Arif', 'Isik', 5389467543, 'KapaliCarsi',8, 'Istanbul', 34777, 'Carsi')")


cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (6, 'home', 'Bafetimbi', 'Gomis', 5543797044, 'Bebek', 11, 'Istanbul', 34876, 'Home')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (6, 'training', 'Bafetimbi', 'Gomis', 5543797044, 'Florya', 2, 'Istanbul', 34854, 'GalatasarayTrainingPlace')")

cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (7, 'home', 'Senol', 'Gunes', 5543797044, 'Fulya', 7, 'Istanbul', 34336, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (7, 'stadium', 'Senol', 'Gunes', 5543797044, 'Besiktas', 8, 'Istanbul', 34974, 'BesiktasStadium')")


cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (8, 'home', 'Oguzhan', 'Ozyakup', 5366799765, 'Tarabya', 22, 'Istanbul', 34393, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (8, 'training', 'Oguzhan', 'Ozyakup', 5366799765, 'Umraniye', 211, 'Istanbul', 34974, 'BesiktasTraining')")

cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (9, 'home', 'Gokhan', 'Gonul', 5343456546, 'Kadikoy', 17, 'Istanbul', 34982, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (9, 'training', 'Gokhan', 'Gonul', 5343456546, 'Umraniye', 92, 'Istanbul', 34875, 'BesiktasTraining')")


cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (10, 'home', 'Anderson', 'Talisca', 5325838888, 'Yenikoy', 17, 'Istanbul', 34779, 'Apartment')")
cursor.execute("INSERT INTO customer_address (u_id, address_title, name, surname,phone_number, street_name,street_number, city, zipcode, address_desc)\
            VALUES (10, 'training', 'Anderson', 'Talisca', 5325838888, 'Besiktas', 29, 'Istanbul', 34974, 'BesiktasStadium')")






conn.commit()
conn.close()
