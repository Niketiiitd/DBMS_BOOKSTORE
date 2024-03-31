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
    Age INT NOT NULL,
    Phone_number BIGINT UNIQUE NOT NULL,
    vendor_password VARCHAR(255) NOT NULL,
	vendor_banned BOOLEAN DEFAULT 0,
    vendor_incorrect_attempts INT DEFAULT 0,
    CONSTRAINT chk_vendor_phone CHECK (Phone_number > 0 AND Phone_number <= 9999999999),
    CONSTRAINT chk_vendor_email CHECK (Email LIKE '%@%'),
    CONSTRAINT chk_password_length CHECK (LENGTH(vendor_password) >= 6),

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
    CONSTRAINT chk_product_price_positive CHECK (book_price >= 0), -- Ensure non-negative product price
    FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
);

-- Customer table
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255),
    Address_ID INT NOT NULL,
    phone_number BIGINT UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    customer_password VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    is_banned BOOLEAN DEFAULT 0,
    incorrect_attempts INT DEFAULT 0,
    CONSTRAINT chk_person_phone CHECK (phone_number > 0 AND phone_number <= 9999999999),
    CONSTRAINT chk_person_email CHECK (email LIKE '%@%'),
    CONSTRAINT chk_person_password_length CHECK (LENGTH(customer_password) >= 6),
    FOREIGN KEY (Address_ID) REFERENCES Address(Address_ID)
);


-- Delivery Agent table
CREATE TABLE IF NOT EXISTS DeliveryAgent (
    daID INT AUTO_INCREMENT PRIMARY KEY,
	da_name VARCHAR(255) NOT NULL,
    da_password VARCHAR(50) NOT NULL,
    availability VARCHAR(20) NOT NULL CHECK (availability IN ('Available', 'Unavailable')),
    da_phone_no BIGINT UNIQUE NOT NULL
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
    Order_status VARCHAR(255) NOT NULL CHECK (Order_status IN ('Scheduled', 'In transit', 'Out for delivery', 'Delivered','Cancelled')),
    orderDATE DATE NOT NULL,
    totalPrice INT NOT NULL,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Book(book_id)
);

-- Product review table
CREATE TABLE IF NOT EXISTS ProductReview (
    review_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    book_id INT NOT NULL,
    customer_id INT NOT NULL,  -- Added column for customer ID
    rating INT NOT NULL,
    content VARCHAR(255) NOT NULL,
    CONSTRAINT chk_vendor_rating_range CHECK (rating >= 0 AND rating <= 5),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)  
);


-- Admin table
CREATE TABLE IF NOT EXISTS MAIN_ADMIN (
    adminID INT NOT NULL PRIMARY KEY,
    hashed_password VARCHAR(70) NOT NULL,
    CONSTRAINT chk_password_complexity CHECK (hashed_password REGEXP '[^a-zA-Z]')
);


-- Cart table
CREATE TABLE IF NOT EXISTS Cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    cart_price BIGINT,
    customer_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    CONSTRAINT chk_quantity_positive CHECK (quantity > 0), -- Ensure quantity is greater than 0
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
  
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);



-- Delivery Agent Review table
CREATE TABLE IF NOT EXISTS DAgentReview (
    da_review_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    daID INT NOT NULL,
    customer_id INT NOT NULL,  
    agent_review INT CHECK (agent_review BETWEEN 1 AND 5),
    agent_review_description VARCHAR(512),
    agent_review_date VARCHAR(50) NOT NULL,
    FOREIGN KEY (daID) REFERENCES DeliveryAgent(daID),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)  -- Added foreign key constraint for customer ID
);


-- Book description table
CREATE TABLE IF NOT EXISTS BookDescription (
    book_description_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    book_id INT NOT NULL,
    book_description VARCHAR(512),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);
CREATE TABLE IF NOT EXISTS customer_order (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    customer_id INT NOT NULL,
    total_price BIGINT NOT NULL,
    order_status VARCHAR(255) NOT NULL DEFAULT 'Pending',
    address VARCHAR(255) NOT NULL,
    payment_mode VARCHAR(255) NOT NULL,
    CONSTRAINT chk_total_price_positive CHECK (total_price >= 0),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);


CREATE TABLE IF NOT EXISTS OrderItem (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES customer_order(order_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
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

CREATE TABLE IF NOT EXISTS StockQuantity (
    stock_quantity_id INT AUTO_INCREMENT NOT NULL,
    isbn_id INT NOT NULL,
    number_of_books INT CHECK (number_of_books > 0), -- Constraint check for positive quantity
    book_type VARCHAR(50),
    PRIMARY KEY (stock_quantity_id, isbn_id),
    FOREIGN KEY (isbn_id) REFERENCES ISBNInfo(isbn_id)
);



-- SELECT host FROM mysql.user WHERE User = 'root';
-- CREATE USER 'root'@'192.168.42.39' IDENTIFIED BY 'Niket@mac';
-- GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.42.39';

-- CREATE USER 'root'@'%' IDENTIFIED BY 'Niket@mac';
-- GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';

-- GRANT ALL PRIVILEGES ON bookshop.* TO 'root'@'192.168.42.39';
-- FLUSH PRIVILEGES;

