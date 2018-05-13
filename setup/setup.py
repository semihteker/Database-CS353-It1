import sqlite3

conn = sqlite3.connect('database.db')
print ("Database created successfully")

conn.execute('''
CREATE TABLE IF NOT EXISTS customer(
    u_id int PRIMARY KEY,
    email varchar(40) ,
    password varchar(20),
    name varchar(20) NOT NULL,
    surname varchar(20) NOT NULL,
    FOREIGN KEY (u_id) REFERENCES user(u_id)
    );''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS phone_number(
    u_id int,
    phone_num varchar(20) NOT NULL,
    FOREIGN KEY (u_id) REFERENCES customer(u_id),
    UNIQUE (phone_num)
    );
''')


conn.execute(
'''
CREATE TABLE IF NOT EXISTS district(
    d_id int,
    district_name varchar(20) NOT NULL,
    area varchar(20) NOT NULL,
    city varchar(20) NOT NULL,
    PRIMARY KEY (d_id)
    );
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS restaurant(
    u_id int,
    email varchar(40),
    password varchar(20),
    name varchar(20) NOT NULL,
    address varchar(60) NOT NULL,
    working_hours varchar(20) NOT NULL,
    isOpen bit NOT NULL,
    rate numeric(3,2),
    d_id int,
    PRIMARY KEY (u_id),
    FOREIGN KEY (u_id) REFERENCES user(u_id),
    FOREIGN KEY (d_id) REFERENCES district(d_id),
    UNIQUE (address),
    UNIQUE (name)
    );
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS rest_phone(
    u_id int,
    phone_num varchar(20) NOT NULL,
    FOREIGN KEY (u_id) REFERENCES restaurant(u_id),
    UNIQUE (phone_num)
    );
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS customer_address(
    u_id int,
    address_type varchar(20) NOT NULL,
    name varchar(20),
    surname varchar(20),
    phone_number varchar(20) NOT NULL,
    street_name varchar(20) NOT NULL,
    street_number numeric(8,0) NOT NULL,
    city varchar(20) NOT NULL,
    zipcode numeric(5,0) NOT NULL,
    adress_desc varchar(80),
    d_id int,
    PRIMARY KEY (u_id, address_type),
    FOREIGN KEY (u_id) REFERENCES customer(u_id),
    FOREIGN KEY (d_id) REFERENCES district(d_id),
    UNIQUE (phone_number)
    );
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS delivery_staff (
    staff_id int AUTO_INCREMENT,
    staff_name varchar(20) NOT NULL,
    PRIMARY KEY (staff_id)
    );
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS product(
    rest_id int,
    food_name varchar(32) NOT NULL,
    food_type varchar(32) NOT NULL,
    price numeric(4,2),
    portion numeric(3,1),
    PRIMARY KEY (rest_id, food_name),
    FOREIGN KEY (rest_id) REFERENCES restaurant(u_id)
    );
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS ingredient(
    ingr_name varchar(32) NOT NULL,
    ingr_calorie varchar(32) NOT NULL,
    quantity numeric(3,1),
    PRIMARY KEY (ingr_name)
    );
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS contains(
    rest_id int,
    food_name varchar(32) NOT NULL,
    ingr_name varchar(32) NOT NULL,
    PRIMARY KEY (rest_id, food_name, ingr_name),
    FOREIGN KEY (rest_id, food_name) REFERENCES product(rest_id, food_name),
    FOREIGN KEY (ingr_name) REFERENCES ingredient(ingr_name)
    );
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS staff_serves(
    d_id int,
    staff_id int,
    FOREIGN KEY (d_id) REFERENCES district(d_id),
    FOREIGN KEY (staff_id) REFERENCES delivery_staff(staff_id));
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS orders(
    ord_id int AUTO_INCREMENT NOT NULL,
    date date NOT NULL,
    order_notes varchar(200),
    source_address varchar(60) NOT NULL,
    dest_address varchar(60) NOT NULL,
    pay_type varchar(40) NOT NULL,
    comment varchar(200),
    rate int,
    cust_id int,
    rest_id int,
    staff_id int,
    PRIMARY KEY (ord_id),
    FOREIGN KEY (rest_id) REFERENCES restaurant(u_id),
    FOREIGN KEY (staff_id) REFERENCES delivery_staff(staff_id));
''')

conn.execute(
'''
CREATE TABLE IF NOT EXISTS comment (
    ord_id int,
    rest_id int,
    food_name varchar(32) NOT NULL,
    PRIMARY KEY (ord_id, rest_id, food_name),
    FOREIGN KEY (ord_id) REFERENCES orders(ord_id),
    FOREIGN KEY (rest_id, food_name) REFERENCES product(rest_id, food_name)
    );
''')
print ("Table created successfully");

conn.close()
