use bookshop;
-- Query to fetch the addresses of customers who have placed orders in the 'Out for delivery' status.

SELECT a.*
FROM Address a
WHERE a.Address_ID IN (
    SELECT c.Address_ID
    FROM Customer c
    JOIN Orders o ON c.customer_id = o.customer_id
    WHERE o.Order_status = 'Out for delivery'
);


-- Subquery to calculate the average rating of books in the ‘Classic’ genre.
SELECT AVG(rating) AS average_rating
FROM ProductReview
WHERE book_id IN (
    SELECT book_id
    FROM Book
    WHERE book_genre = 'Classic'
);

-- Show all delivery agents who have not been reviewed yet.
SELECT DeliveryAgent.daID, DeliveryAgent.da_name
FROM DeliveryAgent
LEFT JOIN DAgentReview ON DeliveryAgent.daID = DAgentReview.daID
WHERE DAgentReview.da_review_id IS NULL;

-- Find the total number of books each vendor has available, along with their names and email addresses. Display only vendors who have more than 10 books. Also show isbn info.
SELECT 
    Vendor.vendor_name,
    Vendor.Email,
    Book.book_title,
    ISBNInfo.isbn_id,
    SUM(StockQuantity.number_of_books) AS total_stock
FROM 
    Vendor
INNER JOIN 
    Book ON Vendor.VendorID = Book.VendorID
INNER JOIN 
    ISBNInfo ON Book.book_id = ISBNInfo.book_id
LEFT JOIN 
    StockQuantity ON ISBNInfo.isbn_id = StockQuantity.isbn_id
WHERE 
    Book.book_availability > 10
GROUP BY 
    Vendor.vendor_name, Vendor.Email, Book.book_title, ISBNInfo.isbn_id;
    
    
    
-- List book titles along with their corresponding authors and the number of reviews they have received, excluding books with no reviews.

SELECT Book.book_title, Book.book_author, COUNT(ProductReview.review_id) AS total_reviews
FROM Book
LEFT JOIN ProductReview ON Book.book_id = ProductReview.book_id
GROUP BY Book.book_title, Book.book_author
HAVING total_reviews > 0;


-- Perform a union on genres ('Dystopian' and 'Adventure') and display all books.
SELECT book_title, book_genre
FROM Book
WHERE book_genre IN (
    SELECT DISTINCT genre
    FROM (
        SELECT 'Dystopian' AS genre
        UNION
        SELECT 'Adventure' AS genre
    ) AS subquery
);

-- Add a 'discount_percentage' column and apply a 10% discount to all books with the genre ‘Fantasy’.
SET SQL_SAFE_UPDATES = 0;

ALTER TABLE Book
ADD COLUMN discount_percentage INT;


UPDATE Book
SET discount_percentage = 10
WHERE book_genre = 'Fantasy';


-- Query to show book genres with an average price greater than 2000.
SELECT book_genre,AVG(book_price) as avg_price
FROM Book
GROUP BY book_genre
HAVING avg_price > 2000;

-- List all books that have not received any reviews yet.

SELECT Book.book_id, Book.book_title
FROM Book
LEFT JOIN ProductReview ON Book.book_id = ProductReview.book_id
WHERE ProductReview.review_id IS NULL;

-- Retrieve the names of customers who have placed orders, along with the total price of their orders. Include customers who have not placed any orders yet, showing a total price of 0 for them.
SELECT Customer.customer_name, COALESCE(SUM(Orders.totalPrice), 0) AS total_price
FROM Customer
LEFT JOIN Orders ON Customer.customer_id = Orders.customer_id
GROUP BY Customer.customer_name;

-- Retrieve the names of customers who have placed orders along with the total price of their orders. Include customers who have not placed any orders yet, displaying a total price of 0 for them. Sort the results by total price in descending order.
SELECT Customer.customer_name, COALESCE(SUM(Orders.totalPrice), 0) AS total_price
FROM Customer
LEFT JOIN Orders ON Customer.customer_id = Orders.customer_id
GROUP BY Customer.customer_name
ORDER BY total_price DESC;





