<?php

  $conn = connectToDB();

  dropTables($conn);
  // $sql = "CREATE TABLE user(
  //         u_id int AUTO_INCREMENT NOT NULL,
  //         email varchar(40) NOT NULL,
  //         password varchar(20) NOT NULL,
  //         PRIMARY KEY (u_id),
  //         UNIQUE (email)
  //         );
  //         ";
  //
  // if (mysqli_query($conn, $sql)) {
  //     echo "Table user is created successfully";
  // } else {
  //     echo "Error creating table: " . mysqli_error($conn);
  // }
  // echo "<br>";
  $sql = "CREATE TABLE customer(
          u_id int,
          email varchar(40) ,
          password varchar(20),
          name varchar(20) NOT NULL,
          surname varchar(20) NOT NULL,
          FOREIGN KEY (u_id) REFERENCES user(u_id)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table customer is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE phone_number(
          u_id int,
          phone_num varchar(20) NOT NULL,
          FOREIGN KEY (u_id) REFERENCES customer(u_id),
          UNIQUE (phone_num)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table phone_number is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE district(
          d_id int,
          district_name varchar(20) NOT NULL,
          area varchar(20) NOT NULL,
          city varchar(20) NOT NULL,
          PRIMARY KEY (d_id)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table district is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE restaurant(
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
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table restaurant is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE rest_phone(
          u_id int,
          phone_num varchar(20) NOT NULL,
          FOREIGN KEY (u_id) REFERENCES restaurant(u_id),
          UNIQUE (phone_num)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table rest_phone is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE customer_address(
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
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table customer_adress is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }


  echo "<br>";
  $sql = "CREATE TABLE delivery_staff (
          staff_id int AUTO_INCREMENT,
          staff_name varchar(20) NOT NULL,
          PRIMARY KEY (staff_id)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table delivery_staff is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE product(
          rest_id int,
          food_name varchar(32) NOT NULL,
          food_type varchar(32) NOT NULL,
          price numeric(4,2),
          portion numeric(3,1),
          PRIMARY KEY (rest_id, food_name),
          FOREIGN KEY (rest_id) REFERENCES restaurant(u_id)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table product is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE ingredient(
          ingr_name varchar(32) NOT NULL,
          ingr_calorie varchar(32) NOT NULL,
          quantity numeric(3,1),
          PRIMARY KEY (ingr_name)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table ingredient is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE contains(
          rest_id int,
          food_name varchar(32) NOT NULL,
          ingr_name varchar(32) NOT NULL,
          PRIMARY KEY (rest_id, food_name, ingr_name),
          FOREIGN KEY (rest_id, food_name) REFERENCES product(rest_id, food_name),
          FOREIGN KEY (ingr_name) REFERENCES ingredient(ingr_name)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table contains is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }



  echo "<br>";
  $sql = "CREATE TABLE staff_serves(
          d_id int,
          staff_id int,
          FOREIGN KEY (d_id) REFERENCES district(d_id),
          FOREIGN KEY (staff_id) REFERENCES delivery_staff(staff_id));
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table staff_serves is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }

  echo "<br>";
  $sql = "CREATE TABLE orders(
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
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table orders is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }


  echo "<br>";
  $sql = "CREATE TABLE comment (
          ord_id int,
          rest_id int,
          food_name varchar(32) NOT NULL,
          PRIMARY KEY (ord_id, rest_id, food_name),
          FOREIGN KEY (ord_id) REFERENCES orders(ord_id),
          FOREIGN KEY (rest_id, food_name) REFERENCES product(rest_id, food_name)
          );
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table comment is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }


  echo "<br>";
  $sql = "CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
              IN p_name VARCHAR(20),
              IN p_surname VARCHAR(20),
              IN p_email VARCHAR(50),
              IN p_password VARCHAR(512)
          )
          BEGIN
              if ( select exists (select 1 from user where email = p_username) ) THEN

                  select 'Email Exists !!';

              ELSE

                  insert into customer
                  (
                      email,
                      password,
                      name,
                      surname
                  )
                  values
                  (
                      p_email,
                      p_password,
                      p_name,
                      p_surname
                  );

              END IF;
          END
          ";

  if (mysqli_query($conn, $sql)) {
      echo "Table comment is created successfully";
  } else {
      echo "Error creating table: " . mysqli_error($conn);
  }


function connectToDB(){

    $db_host = 'localhost';
    $db_user = 'root';
    $db_pwd = '';

    $database = 'rest_express';


    $con = mysqli_connect($db_host, $db_user, $db_pwd);
    if (!$con)
        die("Can't connect to database");

    if (!mysqli_select_db($con,$database))
        die("Can't select database");

    return $con;
}

function dropTables($conn){
  $sql = "SET FOREIGN_KEY_CHECKS = 0;";
  mysqli_query($conn,$sql);



  $table = 'restaurant';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  // $table = 'user';
  // $dropSql = "DROP TABLE IF EXISTS $table;";
  // dropTable($conn,$dropSql,$table);

  $table = 'customer';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'phone_number';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'district';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'rest_phone';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'customer_address';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'delivery_staff';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'product';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'ingredient';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'contains';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'staff_serves';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'comment';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $table = 'orders';
  $dropSql = "DROP TABLE IF EXISTS $table;";
  dropTable($conn,$dropSql,$table);

  $sql = "SET FOREIGN_KEY_CHECKS = 1;";
  mysqli_query($conn,$sql);
}

function dropTable($conn,$sql,$table){
  if (mysqli_query($conn, $sql)) {
      echo "Table $table is dropped successfully";
  } else {
      echo "Error dropping table: " . mysqli_error($conn);
  }
  echo "<br>";
}









 ?>
