CREATE DATABASE IF NOT EXISTS bookshop;
USE bookshop;

-- Utility table
CREATE TABLE IF NOT EXISTS Address (
    Address_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    House_NO INT NOT NULL,
    Street_Name VARCHAR(255),
    City VARCHAR(255) NOT NULL,
    State VARCHAR(255) NOT NULL,
    Zip INT NOT NULL
);

-- Vendor table
CREATE TABLE IF NOT EXISTS Vendor (
    VendorID INT AUTO_INCREMENT PRIMARY KEY,
    vendor_name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) unique NOT NULL,
    Age INT,
    Phone_number BIGINT unique
);

-- Book table
CREATE TABLE IF NOT EXISTS Book (
    book_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    book_title VARCHAR(255) NOT NULL,
    book_author VARCHAR(255) NOT NULL,
    book_genre VARCHAR(255) NOT NULL,
    book_series VARCHAR(255) NOT NULL,
    book_publication VARCHAR(255) NOT NULL,
    book_availability INT NOT NULL,
    VendorID INT,
    book_price INT NOT NULL,
    FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
);

-- Customer table
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    Address_ID INT not null,
    phone_number BIGINT unique NOT NULL,
    email VARCHAR(255) unique NOT NULL,
    customer_password VARCHAR(255) NOT NULL,
    FOREIGN KEY (Address_ID) REFERENCES Address(Address_ID)
);

-- Delivery Agent table
CREATE TABLE IF NOT EXISTS DeliveryAgent (
    daID INT AUTO_INCREMENT PRIMARY KEY,
	da_name VARCHAR(255) NOT NULL,
    da_password VARCHAR(50) NOT NULL,
    availability VARCHAR(20) NOT NULL,
    da_phone_no BIGINT unique NOT NULL
);

-- Warehouse table
CREATE TABLE IF NOT EXISTS Warehouse (
    warehouseID INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255) unique NOT NULL,
    pincode INT NOT NULL
);

-- Orders table
CREATE TABLE IF NOT EXISTS Orders (
    orderID INT AUTO_INCREMENT PRIMARY KEY,
    Order_status VARCHAR(255) NOT NULL,
    orderDATE DATE NOT NULL,
    totalPrice INT NOT NULL
);

-- Product review table
CREATE TABLE IF NOT EXISTS ProductReview (
    review_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    book_id INT NOT NULL,
    rating INT NOT NULL,
    content VARCHAR(255) NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

-- Admin table
CREATE TABLE IF NOT EXISTS Admin (
    adminID INT NOT NULL PRIMARY KEY,
    hashed_password VARCHAR(70) NOT NULL
);

-- Cart table
CREATE TABLE IF NOT EXISTS Cart (
    cart_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cart_price BIGINT,
    customer_id INT NOT NULL,
    book_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

-- Delivery Agent Review table
CREATE TABLE IF NOT EXISTS DAgentReview (
    da_review_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    daID INT NOT NULL,
    agent_review INT,
    agent_review_description VARCHAR(512),
    agent_review_date VARCHAR(50) NOT NULL,
    FOREIGN KEY (daID) REFERENCES DeliveryAgent(daID)
);

-- Book description table
CREATE TABLE IF NOT EXISTS BookDescription (
    book_description_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    book_id INT NOT NULL,
    book_description VARCHAR(512),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

-- Order Item table
CREATE TABLE IF NOT EXISTS OrderItem (
    orderItem_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    book_id INT NOT NULL,
    orderID INT NOT NULL,
    quantity BIGINT,
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (orderID) REFERENCES Orders(orderID)
);

-- ISBN Information table
CREATE TABLE IF NOT EXISTS ISBNInfo (
    isbn_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    book_id INT NOT NULL,
    edition INT,
    date_added VARCHAR(50),
    date_written VARCHAR(50),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

-- Stock Quantity table
CREATE TABLE IF NOT EXISTS StockQuantity (
    stock_quantity_id INT AUTO_INCREMENT NOT NULL,
    isbn_id INT NOT NULL,
    number_of_books INT,
    book_type VARCHAR(50),
    PRIMARY KEY (stock_quantity_id, isbn_id),
    FOREIGN KEY (isbn_id) REFERENCES ISBNInfo(isbn_id)
);






--     
-- select * from customer;
-- select * from books;





-- -- Inserting values in Vendor
-- Insert into vendor(Name,Email,Age,Phone_number)
-- VALUES
-- ('Chetan','chetan@gmail.com',30,9876543210),
-- ('Rahul','rahul@yahoo.com',25,8362572535),
-- ('Yash','yash@gmail.com',22,9562572535);

-- -- Selecting data from the 'vendor' table
-- Select * From vendor;

-- -- Altering Tables Books and customer
-- ALTER TABLE customer
-- MODIFY COLUMN  CustomerID INT AUTO_INCREMENT;
-- Select * from customer;

-- Alter table books
-- MODIFY COLUMN BookID INT AUTO_INCREMENT;

-- -- Inserting Value in Books
-- Insert into books (Title, Author, Genre, Series, Publication, Availability_status, Price, Type)
-- VALUES
-- ('The Great Gatsby','F SCott Fitzgerald', 'Historical fiction','The Great Gatsby', 'Jain', 'Available', 500, 'E-book');

-- -- Selecting data from the 'books' table
-- Select * From books;

-- -- Creating Table  Orders


-- -- Inserting values into orders
-- INSERT INTO  orders (Order_status,orderDATE,totalPrice)
-- VALUES
-- ('Dispatched','2023-12-14',450),
-- ('Delivered','2023-12-16',500),
-- ('Recieved','2023-12-18',800);

-- select * from orders;

-- -- create a table orderitem

-- CREATE TABLE orderItem (
--     quantity INT NOT NULL    
-- );

-- -- insert some values
-- INSERT INTO orderItem (quantity)
-- VALUES 
-- (3),
-- (5),
-- (7),
-- (2),
-- (1),
-- (2),
-- (9),
-- (6),
-- (1),
-- (3);

-- -- fetch some values
-- SELECT * FROM orderItem;

-- -- creating table Admins
-- create table Admins(
--     AdminID int AUTO_INCREMENT PRIMARY KEY,
--     Pass VARCHAR(10) NOT NULL
-- );

-- -- Inserting into Admin
-- insert into admins(Pass) 
-- values 
-- ('admin1'),
-- ('admin2'),
-- ('admin3'),
-- ('admin4');
-- -- Selecting admin details
-- select * from admins;

-- Delete from admins where AdminID > 4; -- Deleting the extra records.



-- Alter Table deliveryAgent
-- MODIFY COLUMN da_password VARCHAR(20) NOT NULL;

-- -- insert some values
-- INSERT INTO deliveryAgent (name,da_password,availability,da_phone_no)
-- VALUES  
-- ("Suresh Singh","abc123", "available", 6666777777),
-- ("Sonu Kumar","xxy67", "not available", 6969696969),
-- ("Gajendra Singh Chauhan","book234", "not available", 9999666888),
-- ("Priyanshu Dwivedi","45priy", "available", 1234567898),
-- ("Satish Pal","ravish456", "available", 4204204204),
-- ("Naveen Nayak","shrishti5", "available", 1212121212),
-- ("Rajendra Gupta","jjk@689", "not available", 8888888889),
-- ("Salman Khan","suhana@nepo", "available", 4444455555),
-- ("Pradeep Kumar","kumar_sahab", "not available", 3453453457),
-- ("Vineet Batra","batra@bkl", "available", 6666778887);

-- -- fetch some values
-- SELECT * FROM deliveryAgent;
-- SELECT * FROM deliveryAgent WHERE availability="available";

-- -- create a table



-- -- insert some values
-- INSERT INTO warehouse (address, pincode)
-- VALUES

-- ("ABC ROAD, FLAT 67", 110092),
-- ("XYZ VIHAR, FLAT 123", 110020),
-- ("QWERTY, HOUSE 78", 110002),
-- ("ABC ROAD, FLAT 80", 110092),
-- ("MG ROAD, 567", 110001),
-- ("ABCDE, 678", 123456),
-- ("JKL, BUILDING 445", 345123),
-- ("INDIA ROAD, FLAT 3", 110090),
-- ("XYZ ROAD, FLAT 67", 110008),
-- ("GHJK ROAD,  45567", 800900);

-- -- Fetching Values
-- select * from warehouse;