-- 7.5 Adjustment page
-- (Data retrieval)
SELECT *
FROM customer
WHERE u_id = @_SESSION[id]

-- Update the table
UPDATE customer
SET name=@_SESSION[name], surname=@_SESSION[surname], email=@_SESSION[email], password=@_SESSION[hashed_password]
WHERE u_id=@_SESSION[id]

-- Delete customer (No Page)
DELETE FROM customer
WHERE u_id = @_SESSION[id]


-- 7.6 Add New Address
-- Insert into
INSERT INTO customer_address (address_type,phone_number,street_name,street_number,city,zipcode,adress_desc,d_id)
                  VALUES (?,?,?,?,'Ankara',?,?,2)

-- 7.7 Edit address
-- Data retrieval
SELECT *
FROM customer_address
WHERE u_id = @_SESSION[id] AND address_type=@_SESSION[address_type]

-- Update the table
UPDATE customer_address
SET address_type=@_SESSION[address_type], phone_number=@_SESSION[phone_number],
  street_name=@_SESSION[street_name], street_number=@_SESSION[street_number],
  city=@_SESSION[city], zipcode=@_SESSION[zipcode],adress_desc=@_SESSION[adress_desc], d_id=@_SESSION[d_id],
WHERE u_id = @_SESSION[id] AND address_type=@_SESSION[address_type]

-- Delete address
DELETE FROM customer_address
WHERE u_id = @_SESSION[id] AND address_type=@_SESSION[address_type]

-- 7.8 List Restaurants Page
SELECT name,rate
FROM restaurant
WHERE d_id = @_SESSION[d_id] AND isOpen=1

-- 7.10 List menus of the Restaurants
SELECT R.food_type,S.food_name,S.totalCalorie,S.price
FROM product R NATURAL JOIN productCalorie S
WHERE R.rest_id = @_SESSION[rest_id]
GROUP BY food_type
