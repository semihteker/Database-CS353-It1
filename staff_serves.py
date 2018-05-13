import sqlite3

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (1)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (2)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (3)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (4)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (5)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (6)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (7)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (8)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (9)")
cursor.execute("INSERT INTO staff_serves( staff_id)\
            VALUES (10)")


conn.commit()
conn.close()
