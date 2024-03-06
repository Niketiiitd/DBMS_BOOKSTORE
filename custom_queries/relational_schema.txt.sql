
-- Address (Address_ID [PK], House_NO, Street_Name, City, State, Zip)
-- Vendor (VendorID [PK], vendor_name, Email, Age, Phone_number)
-- Book (book_id [PK], book_title, book_author, book_genre, book_series, book_publication, book_availability, VendorID [FK], book_price)
-- Customer (customer_id [PK], customer_name, Address_ID [FK], phone_number, email, customer_password, age)
-- DeliveryAgent (daID [PK], da_name, da_password, availability, da_phone_no)
-- Warehouse (warehouseID [PK], address, pincode)
-- Orders (orderID [PK], Order_status, orderDATE, totalPrice, customer_id [FK])
-- ProductReview (review_id [PK], book_id [FK], rating, content)
-- MAIN_ADMIN (adminID [PK], hashed_password)
-- Cart (cart_id [PK], cart_price, customer_id [FK], book_id [FK], quantity)
-- DAgentReview (da_review_id [PK], daID [FK], agent_review, agent_review_description, agent_review_date)
-- BookDescription (book_description_id [PK], book_id [FK], book_description)
-- OrderItem (orderItem_id [PK], book_id [FK], orderID [FK], quantity)
-- ISBNInfo (isbn_id [PK], book_id [FK], edition, date_added, date_written)
-- StockQuantity (stock_quantity_id [PK], isbn_id [FK], number_of_books, book_type)


-- In this representation:
-- - [PK] denotes Primary Key
-- - [FK] denotes Foreign Key