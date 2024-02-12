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
    customer_id INT auto_increment PRIMARY KEY,
    customer_name VARCHAR(255),
    Address_ID INT not null,
    phone_number BIGINT unique NOT NULL,
    email VARCHAR(255) unique NOT NULL,
    customer_password VARCHAR(255) NOT NULL,
    age int not null,
    FOREIGN KEY (Address_ID) REFERENCES Address(Address_ID)
);

-- select * from customer;
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
    pincode INT NOT NULL,
    FOREIGN KEY (Address_ID) REFERENCES Address(Address_ID)
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
CREATE TABLE IF NOT EXISTS MAIN_ADMIN (
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

