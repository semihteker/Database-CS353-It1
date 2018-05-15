import sqlite3

def xyz2():

    conn = sqlite3.connect('setup/database.db')
    cursor = conn.cursor()


    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (1, 'Semih')")
    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (2, 'Berkay')")
    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (3, 'Bahadir')")
    ccursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (4, 'Halil')")
    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (5, 'Gomis')")
    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (6, 'Quaresma')")
    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (7, 'Negredo')")
    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (8, 'Fatih')")
    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (9, 'Babel')")
    cursor.execute("INSERT INTO delivery_staff(staff_id, staff_name)\
                VALUES (10, 'Pepe')")


    conn.commit()
    conn.close()
