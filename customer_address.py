import sqlite3

def xyz();

    conn = sqlite3.connect('setup/database.db')
    cursor = conn.cursor()




    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number, street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (1, 'home', 5544667898,'Cayyolu', 5, 'Ankara', 06554, 'Mesa', 2)")
    cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (1, 'school', 5544647898, 'BilkentUni', 8, 'Ankara', 06000, '74thdormitory', 2)")

    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number, street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (2, 'home', 5224667898, 'Yenimahalle', 3, 'Ankara', 07554, 'Toki', 3)")
    cursor.execute("INSERT INTO customer_address (u_id, address_title, street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (2, 'school', 5384667898, 'BilkentUni', 8, 'Ankara', 06000, EABuilding, 3)")


    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (3, 'home', 5549997898, 'Incek', 5, 'Ankara', 06554, 'Residences', 2)")
    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (3, 'school', 5544667777,'BilkentUni', 8, 'Ankara', 06000, 'ABuilding', 3)")


    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (4, 'home', 5544668888, 'Umitkoy', 5, 'Ankara', 06876, 'Apartment', 1))
    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (4, 'school', 5544669999,'BilkentUni', 8, 'Ankara', 06000, 'BBuilding', 3)")

    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (5, 'home', 5387777543, 'Maslak', 2, 'Istanbul, 34076, 'Apartment', 20)")
    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (5, 'work', 5388984543, 'KapaliCarsi',8, 'Istanbul', 34777, 'Carsi', 17)")


    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (6, 'home', 5544698798, 'Bebek', 11, 'Istanbul', 34876, 'Home', 19)")
    ccursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (6, 'training', 5539877898, 'Florya', 2, 'Istanbul', 34854, 'GalatasarayTrainingPlace', 19)")

    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (7, 'home', 5598667898, 'Fulya', 7, 'Istanbul', 34336, 'Apartment', 18)")
    ccursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (7, 'stadium', 5664667898, 'Besiktas', 8, 'Istanbul', 34974, 'BesiktasStadium', 17)")


    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (8, 'home', 5567897898, 'Tarabya', 22, 'Istanbul', 34393, 'Apartment', 19)")
    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (8, 'training', 5593089768,  'Umraniye', 211, 'Istanbul', 34974, 'BesiktasTraining', 17)")

    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (9, 'home', 5544654673, 'Kadikoy', 17, 'Istanbul', 34982, 'Apartment', 16)")
    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (9, 'training', 5544667232,  'Umraniye', 92, 'Istanbul', 34875, 'BesiktasTraining', 16)")


    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (10, 'home', 5523678998, 'Yenikoy', 17, 'Istanbul', 34779, 'Apartment', 17)")
    cursor.execute("INSERT INTO customer_address (u_id, address_title, phone_number,street_name,street_number, city, zipcode, address_desc, d_id)\
                VALUES (10, 'training', 5447778899, 'Besiktas', 29, 'Istanbul', 34974, 'BesiktasStadium', 17)")






    conn.commit()
    conn.close()

