use bookshop;

-- Inserting a book with a negative price
INSERT INTO Book (book_title, book_author, book_genre, book_series, book_publication, book_availability, VendorID, book_price)
VALUES ('Sample Book', 'John Doe', 'Fiction', 'Sample Series', 'Publisher ABC', 100, 1, -10);

-- Inserting a cart item with a negative quantity
INSERT INTO Cart (cart_price, customer_id, book_id, quantity)
VALUES (100, 1, 1, -1);

-- Inserting a review with a rating greater than 5
INSERT INTO ProductReview (book_id, rating, content)
VALUES (1, 6, 'Great book!');


-- Inserting a new customer with an invalid email format
INSERT INTO Customer (customer_name, Address_ID, phone_number, email, customer_password, age)
VALUES ('John Doe', 1, 1234567890, 'invalid_email', 'password123', 30);


-- Inserting an order item with a negative quantity
INSERT INTO OrderItem (book_id, orderID, quantity)
VALUES (1, 1, -1);
