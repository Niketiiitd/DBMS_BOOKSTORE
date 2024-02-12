create database if not exists bookshop;
use bookshop;
-- utility table 
CREATE TABLE IF NOT EXISTS Address (
    Address_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	House_NO int not null,
    Street_Name VARCHAR(255),
    City VARCHAR(255) not null,
    State VARCHAR(255) not null,
    zip INT NOT NULL
);
-- tables
 
create table if not exists customer(
	customer_id int primary key,
    name varchar(255),
    address varchar(255),
    -- Address_ID INT NOT NULL, 
    FOREIGN KEY (Address_ID) REFERENCES address(Address_ID),
    phone_number int not null,
    email varchar(255) not null,
    Password varchar(255) not null
);


-- create a table

CREATE TABLE deliveryAgent (
    daID INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL,
    da_password varchar(10) NOT NULL,
    availability varchar(20) NOT NULL,
    da_phone_no BIGINT NOT NULL
    
);


CREATE TABLE warehouse (
    warehouseID INT AUTO_INCREMENT PRIMARY KEY,
    address varchar(255) NOT NULL,
    pincode INT NOT NULL    
);

CREATE TABLE orders (
    orderID INT AUTO_INCREMENT PRIMARY KEY,
    Order_status VARCHAR(255) NOT NULL,
    orderDATE DATE NOT NULL,
    totalPrice INT NOT NULL
);

create table prodct_review(
	review_id int auto_increment not null primary key,
    rating int not null,
    content varchar(255) not null
);


create table vendor(
    VendorID INT AUTO_INCREMENT PRIMARY KEY,
    vendor_name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Age INT,
    Phone_number BIGINT
);

create table book(
	book_id int auto_increment not null primary key,
    book_title varchar(50) not null,
    book_author varchar(100) not null,
    book_genre varchar(50) not null,
    book_seires varchar(50) not null,
    book_publication varchar(50) not null,
    book_title varchar(50) not null,
    book_availablity int not null,
    foreign key (VendorID) references vendor(VendorID),
    book_price int not null
    -- isbn to be added
    --  book type to be added
);


-- create table bookDescription(
-- 	description_id INT PRIMARY KEY AUTO_INCREMENT,
-- 	book_id INT,
--     FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
-- );

create table admin(
	adminID int not null primary key,
    hashed_password varchar(70) not null
);
    
    
    

    
select * from customer;
select * from books;

-- Creating Table Vendor



-- Inserting values in Vendor
Insert into vendor(Name,Email,Age,Phone_number)
VALUES
('Chetan','chetan@gmail.com',30,9876543210),
('Rahul','rahul@yahoo.com',25,8362572535),
('Yash','yash@gmail.com',22,9562572535);

-- Selecting data from the 'vendor' table
Select * From vendor;

-- Altering Tables Books and customer
ALTER TABLE customer
MODIFY COLUMN  CustomerID INT AUTO_INCREMENT;
Select * from customer;

Alter table books
MODIFY COLUMN BookID INT AUTO_INCREMENT;

-- Inserting Value in Books
Insert into books (Title, Author, Genre, Series, Publication, Availability_status, Price, Type)
VALUES
('The Great Gatsby','F SCott Fitzgerald', 'Historical fiction','The Great Gatsby', 'Jain', 'Available', 500, 'E-book');

-- Selecting data from the 'books' table
Select * From books;

-- Creating Table  Orders


-- Inserting values into orders
INSERT INTO  orders (Order_status,orderDATE,totalPrice)
VALUES
('Dispatched','2023-12-14',450),
('Delivered','2023-12-16',500),
('Recieved','2023-12-18',800);

select * from orders;

-- create a table orderitem

CREATE TABLE orderItem (
    quantity INT NOT NULL    
);

-- insert some values
INSERT INTO orderItem (quantity)
VALUES 
(3),
(5),
(7),
(2),
(1),
(2),
(9),
(6),
(1),
(3);

-- fetch some values
SELECT * FROM orderItem;

-- creating table Admins
create table Admins(
    AdminID int AUTO_INCREMENT PRIMARY KEY,
    Pass VARCHAR(10) NOT NULL
);

-- Inserting into Admin
insert into admins(Pass) 
values 
('admin1'),
('admin2'),
('admin3'),
('admin4');
-- Selecting admin details
select * from admins;

Delete from admins where AdminID > 4; -- Deleting the extra records.



Alter Table deliveryAgent
MODIFY COLUMN da_password VARCHAR(20) NOT NULL;

-- insert some values
INSERT INTO deliveryAgent (name,da_password,availability,da_phone_no)
VALUES  
("Suresh Singh","abc123", "available", 6666777777),
("Sonu Kumar","xxy67", "not available", 6969696969),
("Gajendra Singh Chauhan","book234", "not available", 9999666888),
("Priyanshu Dwivedi","45priy", "available", 1234567898),
("Satish Pal","ravish456", "available", 4204204204),
("Naveen Nayak","shrishti5", "available", 1212121212),
("Rajendra Gupta","jjk@689", "not available", 8888888889),
("Salman Khan","suhana@nepo", "available", 4444455555),
("Pradeep Kumar","kumar_sahab", "not available", 3453453457),
("Vineet Batra","batra@bkl", "available", 6666778887);

-- fetch some values
SELECT * FROM deliveryAgent;
SELECT * FROM deliveryAgent WHERE availability="available";

-- create a table



-- insert some values
INSERT INTO warehouse (address, pincode)
VALUES

("ABC ROAD, FLAT 67", 110092),
("XYZ VIHAR, FLAT 123", 110020),
("QWERTY, HOUSE 78", 110002),
("ABC ROAD, FLAT 80", 110092),
("MG ROAD, 567", 110001),
("ABCDE, 678", 123456),
("JKL, BUILDING 445", 345123),
("INDIA ROAD, FLAT 3", 110090),
("XYZ ROAD, FLAT 67", 110008),
("GHJK ROAD,  45567", 800900);

-- Fetching Values
select * from warehouse;