-- DDL Statements
-- DDL Statements

-- Driver's information
create table if not exists driver_info(
    dl_number char(16) not null,
    constraint pk_driver_dl primary key(dl_number),
    driver_name varchar(35) not null,
    driver_dob date not null,
    driving_experience int not null,
    available boolean default true
);
alter table driver_info
add constraint check_experience check(driving_experience >= 2);

-- Drivers Contact numbers
create table driver_contacts(
    dl_number char(16) not null,
    constraint fk_driver_dl foreign key(dl_number) references driver_info(dl_number),
    phone_no char(10)
);
alter table driver_contacts 
modify phone_no char(10) not null;
alter table driver_contacts 
add constraint check_phone check(char_length(phone_no) = 10);

-- Customer's information
create table customer_info(
    customer_id int not null auto_increment,
    dl_number char(16) unique,
    firstname varchar(35) not null,
    lastname varchar(35) not null,
    phone_no char(10) not null,
    username varchar(35) not null unique,
    password varchar(50) not null,
    dob date not null,
    email varchar(35),
    state varchar(35) not null,
    city varchar(35) not null,
    street varchar(35) not null,
    zipcode char(5) not null,
    constraint pk_customer_id primary key(customer_id),
    constraint check_phone_customer check(char_length(phone_no) = 10)
);
alter table customer_info auto_increment = 20000;

create table locations(
    location_id int not null auto_increment,
    location_name varchar(50) not null,
    state varchar(35) not null,
    city varchar(35) not null,
    street varchar(35) not null,
    zipcode int(5) not null,
    constraint pk_location_id primary key(location_id)
);
alter table locations auto_increment = 40000;
alter table locations 
modify location_name varchar(50) not null unique;

-- Car Category
create table car_category(
    category_name varchar(35) not null,
    no_persons int not null,
    cost_per_day double not null,
    late_fee_per_hour double not null,
    constraint pk_category_name primary key(category_name)
);

-- Car details
create table car_details(
    registration_no char(6) not null,
    model_name varchar(35) not null,
    make varchar(35) not null,
    model_year int(4) not null,
    mileage double not null,
    available boolean default true,
    category varchar(35) not null,
    car_location int not null,
    constraint pk_car_reg primary key(registration_no),
    constraint fk_car_category foreign key(category) references car_category(category_name),
    constraint fk_car_location foreign key(car_location) references locations(location_id)
);

-- Discount
create table discount(
    coupon_code char(4) not null,
    coupon_name varchar(35) not null,
    discount_percentage double not null,
    expiry_date date not null,
    constraint pk_discount_coupon primary key(coupon_code)
);

-- Booking Details
CREATE TABLE booking_details (
    booking_id SERIAL PRIMARY KEY,
    from_date DATE NOT NULL,
    return_date DATE NOT NULL,
    basic_fare DOUBLE NOT NULL,
    discount_percentage DOUBLE DEFAULT 0,
    booking_status BOOLEAN DEFAULT FALSE,
    with_driver BOOLEAN DEFAULT FALSE,
    actual_return_date DATE NOT NULL,
    pickup_location INT NOT NULL,
    drop_location INT NOT NULL,
    coupon_code CHAR(4),
    car_reg_no CHAR(6) NOT NULL,
    customer_id INT NOT NULL,
    booking_date DATE ,
    CONSTRAINT fk_booking_coupon FOREIGN KEY (coupon_code) REFERENCES discount (coupon_code),
    CONSTRAINT fk_booking_car FOREIGN KEY (car_reg_no) REFERENCES car_details (registration_no),
    CONSTRAINT fk_booking_pickup FOREIGN KEY (pickup_location) REFERENCES locations (location_id),
    CONSTRAINT fk_booking_pickdrop FOREIGN KEY (drop_location) REFERENCES locations (location_id),
    CONSTRAINT fk_booking_customer FOREIGN KEY (customer_id) REFERENCES customer_info (customer_id)
);

alter table booking_details auto_increment=50000;

-- Billing Details
create table billing_details(
    bill_id int not null auto_increment,
    booking_id int not null,
    tax_amount double default 20.0,
    damage_compensation double default 0,
    late_fee double default 0, -- if actual return date > return date
    bill_date date  ,
    constraint pk_bill_id primary key(bill_id),
    constraint fk_bill_booking foreign key(booking_id) references booking_details(booking_id)
);
alter table billing_details auto_increment = 60000;

-- Customer who has booked with driver those detils will be stored here
create table booking_with_driver(
    id int not null auto_increment,
    driver_dl char(16) not null,
    customer_id int not null,
    booking_id int not null,
    booking_date date ,
    constraint pk_driver_customer_id primary key(id),
    constraint fk_booking_driver_customer foreign key(driver_dl) references driver_info(dl_number),
    constraint fk_booking_customer_driver foreign key(customer_id) references customer_info(customer_id),
    constraint fk_booking_id foreign key(booking_id) references booking_details(booking_id)
);

alter table booking_with_driver auto_increment = 70000;


-- driver's data
insert into driver_info values
    ( "HR-0619830034761", "Liam", "1975-01-07", 15, true),
    ( "HR-0619850034771", "Noah", "1970-03-17", 8, false),
    ("HR-0619880034781", "Oliver", "1985-05-20", 10, true),
    ( "HR-0619890034791", "Elijah", "1995-07-11", 6, false),
    ( "HR-0619820034661", "James", "1972-09-18", 20, true);

-- driver's contacts
insert into driver_contacts values
    ("HR-0619830034761", 9982641789),
    ("HR-0619830034761", 9927593732),
    ("HR-0619850034771", 8535919898),
    ("HR-0619880034781", 9972104143),
    ("HR-0619890034791", 6363212645),
    ("HR-0619890034791", 7676676566),
    ("HR-0619820034661", 9591858426);

-- Customers info
insert into customer_info( dl_number, firstname, lastname, phone_no, username, password, dob, email, state, city, street, zipcode ) values
    ( "HR-0719830034891", "Adler", "Anderson", 8322335022, "alderanderson", "1234@", "2000-02-04", "alderanderson@gmail.com", "Alabama", "Montgomery", "Main Street.", 40202 ),
    ( "HR-0719830034892", "Seth", "Ivan", 7926870547, "sethivan", "abcd@", "2002-03-05", "sethivan@gmail.com", "Alaska", "Juneau", "2nd Street.", 40203 ),
    ( "HR-0719830034893", "Riley", "Gilbert", 9822334254, "rileygilbert", "wxyz@", "1975-04-06", "rileygilbert@gmail.com", "Arizona", "Phoenix", "7th Street.", 40204),
    ( null, "Jorge", "Dan", 9841310497, "jorgedan", "1234@", "1980-05-07", null, "Arkansas", "Little Rock", "3rd Street.", 40205 ),
    ( "HR-0719830034895", "Brian", "Roberto", 9998958055, "brianroberto", "abcd@", "2003-06-08", "brianroberto@gmail.com", "California", "Sacramento", "1st Street.", 40207 ),
    ( null, "Ramon", "Miles", 7759228501, "ramonmiles", "wxyz@", "2005-07-09", "ramonmiles@gmail.com", "Alabama", "Montgomery", "Main Street", 40202),
    ("HR-0719830034897","Liam","Nathaniel",8212415127,"liamnathaniel","1234@","1960-08-10","liamnathaniel@gmail.com","Alabama","Montgomery","Main Street",40202);

-- Locations
insert into locations(location_name, state, city, street, zipcode) VALUES
    ( 'Private AIRPORT', "Alabama", "Montgomery", "Main Street.", 40202 ),
    ( 'DALLAS LOVE FIELD AIRPORT', "Alabama", "Montgomery", "Main Street.", 40202 ),
    ( 'LOS ANGELES INTL AIRPORT', "Alaska", "Juneau", "2nd Street.", 40203 ),
    ( 'DALLAS/ FORT WORTH INTL AIRPORT', "Alabama", "Montgomery", "Main Street.", 40202 ),
    ( 'WEST HOUSTON AIRPORT', "Arizona", "Phoenix", "7th Street.", 40204),
    ( 'WASHINGTON DULLES INTL AIRPORT', "California", "Sacramento", "1st Street.", 40207);

-- car category
insert into car_category values
    ('ECONOMY', 5, 30, 0.9),
    ('COMPACT', 5, 32, 0.96),
    ('MID SIZE', 5, 35, 1.05),
    ('STANDARD', 5, 38, 1.14),
    ('FULL SIZE', 5, 40, 1.2),
    ('LUXURY CAR', 5, 75, 2.25),
    ('MID SIZE SUV', 5, 36, 1.08),
    ('STANDARD SUV', 5, 40, 1.2),
    ('FULL SIZE SUV', 8, 60, 1.8),
    ('MINI VAN', 7, 70, 2.1);

-- Car Details
insert into car_details( registration_no, model_name, make, model_year,category,mileage) values
    ( 'AB1234', 'CIVIC', 'HONDA', 2014, 8, 'ECONOMY', 40000),
    ( 'SD4567', 'FIESTA', 'FORD', 2015, 6, 'ECONOMY', 40001),
    ( 'GLZ2376', 'COROLLA', 'TOYOTA', 2016, 5.000, 'ECONOMY', 40002),
    ( 'WER3245', 'ACCENT', 'HYUNDAI', 2014, 12.356, 'ECONOMY', 40003),
    ( 'HJK1234', 'CIVIC', 'HONDA', 2015, 20.145, 'ECONOMY', 40004),
    ( 'GLS7625', 'FOCUS', 'FORD', 2014, 12.01, 'COMPACT', 40001),
    ( 'FKD8202', 'GOLF', 'VOLKSWAGAN', 2016, 11.5, 'COMPACT', 40002),
    ( 'HNX1890', 'PRIUS', 'TOYOTA', 2015, 7.8, 'COMPACT', 40003),
    ( 'KJS1983', 'PRIUS', 'TOYOTA', 2014, 9.5, 'COMPACT', 40004),
    ( 'SDL9356', 'FOCUS', 'FORD', 2016, 10, 'COMPACT', 40003),
    ( 'OTY7293', 'CRUZE', 'CHEVROLET', 2016, 14, 'MID SIZE', 40002);

-- discount details
insert into discount( coupon_code, coupon_name, expiry_date, discount_percentage) values
    ( 'D678', 'IBM CORPORATE', '2023-01-25', 25),
    ( 'D234', 'CTS CORPORATE', '2024-09-02', 20),
    ( 'D109', 'WEEKLY RENTALS', '2022-11-09', 25),
    ( 'D972', 'ONE WAY SPECIAL', '2023-12-15', 20),
    ( 'D297', 'UPGRADE SPECIAL', '2025-02-18', 20),
    ( 'D756', 'HOLIDAY SPECIAL', '2021-10-29', 10);


-- Queries
-- To fetch all available cars
select * from car_details, car_category where category = category_name and available = true order by cost_per_day;

select * from car_details inner join car_category on category = category_name and available = true order by cost_per_day;

-- To fetch all car category names
select category_name from car_category;

-- To fetch all cars by category 
select * from car_details, car_category where category = category_name and available = true  and  category_name = "economy" order by cost_per_day;


-- Join Queries
-- 1. select all available car details
select * from car_details inner join car_category on category = category_name where available = true order by cost_per_day;

-- 2. Show car details along with its current location.
select * from car_details inner join locations on car_location = location_id;

-- 3. Show cars booked by customers.
select Firstname,Lastname, model_name from customer_info join 
(booking_details join car_details) where customer_info.Customer_ID = 
booking_details.Customer_ID and Registration_No = Car_Reg_No;

-- 4.  Display Car Details along with along with the category to which it belongs, No of persons it can hold, Cost per day
select * from car_details inner join car_category on category = category_name order by cost_per_day;

-- Aggregate Functions
-- number of bookings by each customer
select username as CustomerName, count(*) as NoOfTimes from booking_details as B inner join customer_info as C on B.customer_id = C.customer_id  group by c.username order by NoOfTimes desc;

-- Total No of bookings till date
select count(*) as TotalBookings from booking_details order by TotalBookings;

-- No. of cars booked on particular date
select booking_date as OnDate, count(*) as CarsBooked from booking_details group by booking_date;

-- No of cars belong to each category
select category, count(*) as NoOfCars from car_details group by category;

-- Set Operations
-- 1. Display the Customer First name and Last Name who have returned the Car on or before the Return Date
select Firstname,Lastname from customer_info join booking_details where 
customer_info.Customer_ID = booking_details.Customer_ID and Return_Date = 
Actual_Return_Date
UNION
select Firstname,Lastname from customer_info join booking_details where 
customer_info.Customer_ID = booking_details.Customer_ID and Return_Date > 
Actual_Return_Date;

-- 2. Display the Car that were Booked and the Model_Year >2017
SELECT Make, Model,Model_Year
FROM car_datails cd
JOIN booking_details bd ON cd.Registration_No=bd.Car_Reg_No
WHERE NOT EXISTS (
    SELECT 1
    FROM car_detail
    WHERE Registration_No =cd.Registration_No
    AND Model_Year<=2012
    );



-- Triggers
-- Trigger to update billing_details after car return
drop trigger if exists on_update_return_date;
delimiter $$
create trigger on_update_return_date
after update
on booking_details for each row
begin
    DECLARE extra_hours int;
    DECLARE latefee double;
    
    if date(new.actual_return_date) > date(new.return_date) THEN
        set extra_hours = timestampdiff(hour, new.return_date, new.actual_return_date) + 1;
        select late_fee_per_hour into latefee from car_details, car_category where car_details.category = car_category.category_name and car_details.registration_no = new.car_reg_no;
        update billing_details set late_fee = latefee * extra_hours where booking_id = new.booking_id;
    end if; 

    update car_details set available = true where registration_no = new.car_reg_no;

end $$
delimiter ;

-- After insert into booking_details mark car availability = false
drop trigger if exists after_booking;
delimiter $$
create trigger after_booking
after insert
on booking_details for each row
begin

update car_details set available = false where registration_no = new.car_reg_no;
insert into billing_details(booking_id) values(new.booking_id);

end $$
delimiter ;

-- After insert in driver_customer set driver availability = false
drop trigger if exists after_driver_customer;
delimiter $$
create trigger after_driver_customer
after insert
on booking_with_driver for each row
begin

update driver_info set available = false where dl_number = new.driver_dl;

end $$
delimiter ;

-- Functions
-- Function to calculate driver charge based on experience
drop function if exists driver_charge;
DELIMITER $

CREATE FUNCTION driver_charge (experience int)
  RETURNS double
   DETERMINISTIC
    BEGIN
     DECLARE charge double;
        IF experience > 3 and experience < 6
            THEN SET charge = 500.0;
        ELSEIF  experience > 5 and experience < 10
            THEN SET charge = 700.0;
        ELSEIF  experience >= 10
            THEN SET charge = 1000.0;
        ELSE set charge = 0;
        END IF;
     RETURN charge;
    END $
delimiter ;


-- Procedures
-- Procedure to calculate total amount
drop procedure if exists get_total_amount;
delimiter $

create Procedure get_total_amount(IN bookingid INT, OUT total_amount double)
begin
    DECLARE driver_experience_p int default 0;

    select book.basic_fare + book.basic_fare * bill.tax_amount/100 + bill.damage_compensation + bill.late_fee
    into total_amount from billing_details as bill, booking_details as book 
    where bill.booking_id = book.booking_id and book.booking_id = bookingid;
end $

delimiter ;


-- create a prodecudre to dispalay the car booked on specific date  with driver details
drop procedure if exists car_booked_on_date;
delimiter $
create procedure car_booked_on_date(in given_date date) 
begin
    select B.car_reg_no, di.dl_number,di.driver_name, di.driver_dob, di.driving_experience, di.available, b.booking_date 
    from booking_details as B inner join booking_with_driver as D on B.booking_id = D.booking_id inner join driver_info as di on D.driver_dl = di.dl_number where b.booking_date = given_date;
end $

delimiter ;


-- Cursor
drop procedure if exists createUsernameList;
DELIMITER $$
CREATE PROCEDURE createUsernameList (
	INOUT usernameList varchar(4000)
)
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
	DECLARE user_name varchar(100) DEFAULT "";

	-- declare cursor for employee email
	DEClARE curUsername 
		CURSOR FOR 
			SELECT username FROM customer_info;

	-- declare NOT FOUND handler
	DECLARE CONTINUE HANDLER 
        FOR NOT FOUND SET finished = 1;

	OPEN curUsername;

	getUsername: LOOP
		FETCH curUsername INTO user_name;
		IF finished = 1 THEN 
			LEAVE getUsername;
		END IF;
		-- build email list
		SET usernameList = CONCAT(user_name,";",usernameList);
	END LOOP getUsername;
	CLOSE curUsername;

END$$
DELIMITER ;
