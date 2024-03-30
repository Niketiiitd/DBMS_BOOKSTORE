use bookshop;


INSERT INTO Address (House_NO, Street_Name, City, State, Zip) VALUES
(123, 'Main Street', 'New York City', 'New York', 10001),
(456, 'Elm Street', 'Los Angeles', 'California', 90001),
(789, 'Oak Avenue', 'Chicago', 'Illinois', 60601),
(1011, 'Pine Road', 'Houston', 'Texas', 77001),
(1213, 'Cedar Lane', 'Phoenix', 'Arizona', 85001),
(1415, 'Maple Drive', 'Philadelphia', 'Pennsylvania', 19101),
(1617, 'Cherry Street', 'San Antonio', 'Texas', 78201),
(1819, 'Sycamore Street', 'San Diego', 'California', 92101),
(2021, 'Willow Avenue', 'Dallas', 'Texas', 75201),
(2223, 'Birch Boulevard', 'San Jose', 'California', 95101),
(2425, 'Ash Street', 'Austin', 'Texas', 73301),
(2627, 'Hickory Lane', 'Jacksonville', 'Florida', 32099),
(2829, 'Poplar Court', 'Indianapolis', 'Indiana', 46201),
(3031, 'Peach Street', 'San Francisco', 'California', 94101),
(3233, 'Plum Road', 'Columbus', 'Ohio', 43201),
(3435, 'Chestnut Avenue', 'Charlotte', 'North Carolina', 28201),
(3637, 'Beech Drive', 'Seattle', 'Washington', 98101),
(3839, 'Walnut Lane', 'Denver', 'Colorado', 80201),
(4041, 'Grove Street', 'Detroit', 'Michigan', 48201),
(4243, 'Spruce Court', 'Boston', 'Massachusetts', 02101);




INSERT INTO Vendor (vendor_name, Email, Age, Phone_number) VALUES
('Oliver', 'oliverrr@example.com', 35, 1234567896),
('June', 'june@example.com', 40, 2345678901),
('Agust', 'agust@example.com', 45, 3456789012),
('Sophia', 'sophia@example.com', 50, 4567890123),
('Ethan', 'ethan@example.com', 55, 5678901234),
('Emma', 'emma@example.com', 60, 6789012345),
('Mia', 'mia@example.com', 65, 7890123456),
('James', 'james@example.com', 70, 8901234567),
('Ava', 'ava@example.com', 75, 9012345678),
('William', 'william@example.com', 80, 1234567890),
('Olivia', 'olivia@example.com', 85, 2345678902),
('Isaac', 'isaac@example.com', 90, 3456789013),
('Charlotte', 'charlotte@example.com', 95, 4567890124),
('Amelia', 'amelia@example.com', 100, 5678901235),
('Michael', 'michael@example.com', 105, 6789012346),
('Emma', 'emma2@example.com', 110, 7890123457),
('Jacob', 'jacob@example.com', 115, 8901234568),
('Abigail', 'abigail@example.com', 120, 9012345679),
('Elijah', 'elijah@example.com', 125, 1234567895),
('Sophia', 'sophia2@example.com', 130, 2345678908);


-- delete from Vendor;
-- ALTER TABLE Vendor AUTO_INCREMENT = 1;
-- select * from Vendor;


INSERT INTO Book (book_title, book_author, book_genre, book_series, book_publication, book_availability, VendorID, book_price) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 'Gatsby Series', 'Scribner', 10, 1, 1500),
('To Kill a Mockingbird', 'Harper Lee', 'Classic', 'Maycomb Chronicles', 'J.B. Lippincott & Co.', 15, 2, 1700),
('1984', 'George Orwell', 'Dystopian', 'Orwellian Series', 'Secker & Warburg', 20, 3, 1600),
('Pride and Prejudice', 'Jane Austen', 'Romance', 'Austen Classics', 'T. Egerton, Whitehall', 25, 4, 1800),
('The Catcher in the Rye', 'J.D. Salinger', 'Coming-of-Age', 'Rye Series', 'Little, Brown and Company', 30, 5, 1900),
('Brave New World', 'Aldous Huxley', 'Dystopian', 'World Series', 'Chatto & Windus', 35, 6, 2000),
('To the Lighthouse', 'Virginia Woolf', 'Modernist', 'Lighthouse Collection', 'Hogarth Press', 40, 7, 2100),
('Animal Farm', 'George Orwell', 'Satire', 'Farm Chronicles', 'Secker & Warburg', 45, 8, 2200),
('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 'Middle-Earth Series', 'George Allen & Unwin', 50, 9, 2300),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 'Middle-Earth Series', 'George Allen & Unwin', 55, 10, 2400),
('Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 'Fantasy', 'Harry Potter', 'Bloomsbury', 60, 11, 2500),
('Moby-Dick', 'Herman Melville', 'Adventure', 'Whale Chronicles', 'Harper & Brothers', 65, 12, 2600),
('Ulysses', 'James Joyce', 'Modernist', 'Irish Saga', 'Sylvia Beach', 70, 13, 2700),
('The Odyssey', 'Homer', 'Epic', 'Greek Epics', 'Oxford University Press', 75, 14, 2800),
('Don Quixote', 'Miguel de Cervantes', 'Satire', 'Quixote Chronicles', 'Francisco de Robles', 80, 15, 2900),
('War and Peace', 'Leo Tolstoy', 'Historical Fiction', 'Tolstoy Collection', 'The Russian Messenger', 85, 16, 3000),
('The Brothers Karamazov', 'Fyodor Dostoevsky', 'Philosophical Fiction', 'Russian Classics', 'The Russian Messenger', 90, 17, 3100),
('The Picture of Dorian Gray', 'Oscar Wilde', 'Gothic', 'Gray Series', 'Ward, Lock and Company', 95, 18, 3200),
('Alice''s Adventures in Wonderland', 'Lewis Carroll', 'Fantasy', 'Wonderland Series', 'Macmillan', 100, 19, 3300),
('Frankenstein', 'Mary Shelley', 'Gothic', 'Frankenstein Series', 'Lackington, Hughes, Harding, Mavor & Jones', 105, 20, 3400);


-- delete from Book;
-- ALTER TABLE Book AUTO_INCREMENT = 1;
-- select * from Book;

-- Insert 20 entries into the Customer table
INSERT INTO Customer (customer_name, Address_ID, phone_number, email, customer_password, age) VALUES
('John Doe', 1, 1234567890, 'john@example.com', 'password1', 30),
('Jane Smith', 2, 2345678901, 'jane@example.com', 'password2', 25),
('Michael Johnson', 3, 3456789010, 'michael@example.com', 'password3', 35),
('Emily Davis', 4, 4567890121, 'emily@example.com', 'password4', 28),
('Christopher Wilson', 5, 5678901232, 'christopher@example.com', 'password5', 40),
('Amanda Martinez', 6, 6789012343, 'amanda@example.com', 'password6', 22),
('David Anderson', 7, 7890123454, 'david@example.com', 'password7', 33),
('Jessica Taylor', 8, 8901234565, 'jessica@example.com', 'password8', 29),
('James Brown', 9, 9012345676, 'james@example.com', 'password9', 45),
('Sarah Thomas', 10, 1234567897, 'sarah@example.com', 'password10', 27),
('Matthew White', 11, 2345678908, 'matthew@example.com', 'password11', 32),
('Jennifer Lee', 12, 3456789019, 'jennifer@example.com', 'password12', 38),
('Daniel Harris', 13, 4567890122, 'daniel@example.com', 'password13', 24),
('Elizabeth Clark', 14, 5678901233, 'elizabeth@example.com', 'password14', 41),
('Christopher Martinez', 15, 6789012344, 'christopher2@example.com', 'password15', 26),
('Linda Lewis', 16, 7890123455, 'linda@example.com', 'password16', 34),
('Thomas Robinson', 17, 8901234566, 'thomas@example.com', 'password17', 31),
('Patricia Walker', 18, 9012345677, 'patricia@example.com', 'password18', 39),
('Matthew Hall', 19, 1234567898, 'matthew2@example.com', 'password19', 36),

('Karen Young', 20, 2345678909, 'karen@example.com', 'password20', 23);

INSERT INTO Customer (customer_name, Address_ID, phone_number, email, customer_password, age) VALUES
('Niket',19,8619631019,'niket@email.com','pass@123',19);

INSERT INTO DeliveryAgent (da_name, da_password, availability, da_phone_no) VALUES
('John Smith', 'agentpassword1', 'Available', 1111111111),
('Emily Johnson', 'agentpassword2', 'Available', 2222222222),
('Michael Williams', 'agentpassword3', 'Available', 3333333333),
('Jessica Brown', 'agentpassword4', 'Available', 4444444444),
('William Miller', 'agentpassword5', 'Available', 5555555555),
('Sophia Davis', 'agentpassword6', 'Available', 6666666666),
('James Wilson', 'agentpassword7', 'Available', 7777777777),
('Olivia Garcia', 'agentpassword8', 'Available', 8888888888),
('Daniel Martinez', 'agentpassword9', 'Available', 9999999999),
('Emma Hernandez', 'agentpassword10', 'Available', 1010101010),
('Liam Lopez', 'agentpassword11', 'Available', 1212121212),
('Ava Gonzalez', 'agentpassword12', 'Available', 1313131313),
('Noah Perez', 'agentpassword13', 'Available', 1414141414),
('Isabella Torres', 'agentpassword14', 'Available', 1515151515),
('Sophia Rivera', 'agentpassword15', 'Available', 1616161616),
('Lucas Long', 'agentpassword16', 'Available', 1717171717),
('Mia Flores', 'agentpassword17', 'Available', 1818181818),
('Benjamin Evans', 'agentpassword18', 'Available', 1919191919),
('Evelyn Reed', 'agentpassword19', 'Available', 2020202020),
('Alexander Wood', 'agentpassword20', 'Available', 2121212121);



INSERT INTO Warehouse (address, pincode) VALUES
('123 Main Street, Cityville, CA', 12345),
('456 Elm Street, Townburg, NY', 23456),
('789 Oak Street, Villageton, TX', 34567),
('321 Pine Street, Hamletown, FL', 45678),
('654 Maple Street, Suburbia, WA', 56789),
('987 Birch Street, Countryside, GA', 67890),
('135 Cedar Street, Villaville, IL', 78901),
('246 Spruce Street, Forestville, MI', 89012),
('357 Cherry Street, Uptown, MA', 90123),
('468 Walnut Street, Seaside, OR', 11223),
('579 Poplar Street, Hillside, CO', 22334),
('680 Sycamore Street, Lakeside, AZ', 33445),
('791 Ash Street, Riverside, NV', 44556),
('802 Oakwood Street, Mountainview, UT', 55667),
('913 Pinecrest Street, Lakeshore, VA', 66778),
('124 Elmwood Street, Parkside, NH', 77889),
('235 Maplewood Street, Hillcrest, NC', 88990),
('346 Cedarwood Street, Beachside, WI', 99001),
('457 Birchwood Street, Riverside, SC', 11222),
('568 Oakhill Street, Valleyview, KY', 22333);

INSERT INTO Orders (Order_status, orderDATE, totalPrice, customer_id) VALUES
('Scheduled', '2024-01-01', 150, 1),
('Delivered', '2024-01-02', 200, 2),
('Cancelled', '2024-01-03', 100, 3),
('Scheduled', '2024-01-04', 250, 4),
('Out for delivery', '2024-01-05', 300, 5),
('Scheduled', '2024-01-06', 180, 6),
('Scheduled', '2024-01-07', 220, 7),
('Delivered', '2024-01-08', 190, 8),
('Cancelled', '2024-01-09', 210, 9),
('Scheduled', '2024-01-10', 170, 10),
('Delivered', '2024-01-11', 280, 1),
('Cancelled', '2024-01-12', 320, 2),
('Scheduled', '2024-01-13', 230, 3),
('Delivered', '2024-01-14', 270, 4),
('Scheduled', '2024-01-15', 150, 5),
('Scheduled', '2024-01-16', 200, 6),
('Out for delivery', '2024-01-17', 180, 7),
('Scheduled', '2024-01-18', 250, 8),
('Delivered', '2024-01-19', 300, 9),
('Scheduled', '2024-01-20', 220, 10);



INSERT INTO ProductReview (book_id, customer_id, rating, content) VALUES
(1, 1, 5, 'This book was fantastic! I couldn''t put it down.'),
(1, 2, 4, 'Enjoyed reading this book, although the ending felt rushed.'),
(2, 3, 2, 'The plot was interesting, but the writing style was not my favorite.'),
(3, 4, 5, 'Absolutely loved this book! Highly recommend it to everyone.'),
(4, 5, 2, 'Disappointed with this book. Expected more from the author.'),
(5, 6, 4, 'A gripping read with well-developed characters.'),
(6, 7, 5, 'One of the best books I''ve read this year!'),
(7, 8, 3, 'An okay read, but nothing memorable.'),
(8, 9, 5, 'Couldn''t stop reading until I finished!'),
(9, 10, 4, 'Solid book with an unexpected twist.'),
(10, 11, 2, 'Found it difficult to get into this book.'),
(11, 12, 5, 'Captivating storyline and beautifully written.'),
(12, 13, 3, 'Started off slow but picked up towards the end.'),
(13, 14, 4, 'Enjoyed the character development throughout.'),
(14, 15, 1, 'Didn''t enjoy this book at all. Not my cup of tea.'),
(15, 16, 5, 'A must-read for fans of the genre!'),
(16, 17, 4, 'Thoroughly enjoyed every page of this book.'),
(17, 18, 3, 'Had some good moments but overall fell short.'),
(17, 19, 5, 'Couldn''t recommend this book enough!'),
(20, 20, 2, 'Struggled to connect with the story and characters.');

INSERT INTO ProductReview (book_id, customer_id, rating, content) VALUES
(20, 21, 2, 'Struggled to connect with the story and characters.');
INSERT INTO MAIN_ADMIN (adminID, hashed_password) VALUES
(1, 'Password1!'),
(2, 'Secure@123'),
(3, 'Admin#2024'),
(4, 'P@55w0rd'),
(5, 'Adm1n_P@ss!');






-- Populating DAgentReview table with data
INSERT INTO DAgentReview (daID, customer_id, agent_review, agent_review_description, agent_review_date) VALUES
(1, 1, 4, 'Prompt and courteous service.', '2024-02-10'),
(2, 2, 5, 'Excellent communication and timely delivery.', '2024-02-11'),
(3, 3, 3, 'Satisfactory service but could be improved.', '2024-02-12'),
(4, 4, 4, 'Professional behavior and efficient service.', '2024-02-13'),
(5, 5, 5, 'Highly satisfied with the delivery agent.', '2024-02-14'),
(6, 6, 2, 'Delivery delayed without prior notice.', '2024-02-15'),
(7, 7, 4, 'Good service overall.', '2024-02-16'),
(8, 8, 3, 'Delivery agent was polite but delivery was late.', '2024-02-17'),
(10, 9, 4, 'Timely delivery and good communication.', '2024-02-19'),
(11, 10, 3, 'Average service, room for improvement.', '2024-02-20'),
(12, 11, 5, 'Exceptional service, highly recommended.', '2024-02-21'),
(13, 12, 2, 'Package arrived damaged, could improve handling.', '2024-02-22'),
(14, 13, 4, 'Professional behavior and timely delivery.', '2024-02-23'),
(15, 14, 5, 'Delivery agent went above and beyond expectations.', '2024-02-24'),
(16, 15, 3, 'Service was okay, could be better.', '2024-02-25'),
(17, 16, 4, 'No issues with the delivery, satisfied overall.', '2024-02-26'),
(18, 17, 5, 'Excellent service, would use again.', '2024-02-27'),
(20, 21, 4, 'Smooth and hassle-free delivery process.', '2024-02-29');


INSERT INTO BookDescription (book_id, book_description) VALUES
(1, 'A thrilling adventure novel set in a post-apocalyptic world where survival is the key.'),
(2, 'A heartwarming tale of friendship and loyalty amidst the chaos of war.'),
(3, 'A gripping mystery novel that will keep you guessing until the very end.'),
(4, 'An epic fantasy saga filled with magic, dragons, and ancient prophecies.'),
(5, 'A poignant coming-of-age story set against the backdrop of a small town.'),
(6, 'A collection of short stories exploring the complexities of human nature.'),
(7, 'A riveting political thriller set in the heart of a corrupt city.'),
(8, 'An insightful memoir recounting the author''s journey of self-discovery.'),
(9, 'A captivating romance novel that will sweep you off your feet.'),
(10, 'An inspiring self-help book offering practical advice for personal growth.'),
(11, 'A chilling horror story guaranteed to send shivers down your spine.'),
(12, 'A thought-provoking exploration of the meaning of life and existence.'),
(13, 'A heart-wrenching tale of love and loss set against the backdrop of war.'),
(14, 'An action-packed adventure novel filled with twists and turns at every corner.'),
(15, 'A captivating historical fiction novel transporting readers to a bygone era.'),
(16, 'A humorous satire poking fun at the absurdities of modern society.'),
(17, 'A gripping psychological thriller that will keep you on the edge of your seat.'),
(18, 'An enchanting fairy tale retelling with a unique twist.'),
(19, 'A compelling science fiction epic exploring the possibilities of the future.'),
(20, 'A touching family drama about the bonds that hold us together in times of adversity.');




-- Inserting data into ISBNInfo table
INSERT INTO ISBNInfo (book_id, edition, date_added, date_written) VALUES
(1, 1, '2023-01-15', '1925-04-10'),  -- The Great Gatsby - 1st Edition - Added: 2023-01-15, Written: 1925-04-10
(2, 2, '2022-12-20', '1960-07-11'),  -- To Kill a Mockingbird - 2nd Edition - Added: 2022-12-20, Written: 1960-07-11
(3, 3, '2023-02-05', '1949-06-08'),  -- 1984 - 3rd Edition - Added: 2023-02-05, Written: 1949-06-08
(4, 2, '2023-02-12', '1813-01-28'),  -- Pride and Prejudice - 2nd Edition - Added: 2023-02-12, Written: 1813-01-28
(5, 1, '2023-03-20', '1951-07-16'),  -- The Catcher in the Rye - 1st Edition - Added: 2023-03-20, Written: 1951-07-16
(6, 1, '2023-04-05', '1932-01-01'),  -- Brave New World - 1st Edition - Added: 2023-04-05, Written: 1932-01-01
(7, 3, '2023-05-10', '1927-05-05'),  -- To the Lighthouse - 3rd Edition - Added: 2023-05-10, Written: 1927-05-05
(8, 1, '2023-06-18', '1945-08-17'),  -- Animal Farm - 1st Edition - Added: 2023-06-18, Written: 1945-08-17
(9, 2, '2023-07-25', '1954-07-29'),  -- The Lord of the Rings - 2nd Edition - Added: 2023-07-25, Written: 1954-07-29
(10, 1, '2023-08-10', '1937-09-21'),  -- The Hobbit - 1st Edition - Added: 2023-08-10, Written: 1937-09-21
(11, 1, '2023-09-15', '1997-06-26'),  -- Harry Potter and the Philosopher's Stone - 1st Edition - Added: 2023-09-15, Written: 1997-06-26
(12, 2, '2023-10-01', '1851-10-18'),  -- Moby-Dick - 2nd Edition - Added: 2023-10-01, Written: 1851-10-18
(13, 1, '2023-11-20', '1922-02-02'),  -- Ulysses - 1st Edition - Added: 2023-11-20, Written: 1922-02-02
(14, 3, '2023-12-05', '800 BCE'),     -- The Odyssey - 3rd Edition - Added: 2023-12-05, Written: 800 BCE
(15, 1, '2024-01-10', '1605-01-16'),  -- Don Quixote - 1st Edition - Added: 2024-01-10, Written: 1605-01-16
(16, 1, '2024-02-20', '1869-01-01'),  -- War and Peace - 1st Edition - Added: 2024-02-20, Written: 1869-01-01
(17, 2, '2024-03-15', '1880-11-26'),  -- The Brothers Karamazov - 2nd Edition - Added: 2024-03-15, Written: 1880-11-26
(18, 1, '2024-04-30', '1890-07-01'),  -- The Picture of Dorian Gray - 1st Edition - Added: 2024-04-30, Written: 1890-07-01
(19, 1, '2024-05-12', '1865-11-26'),  -- Alice's Adventures in Wonderland - 1st Edition - Added: 2024-05-12, Written: 1865-11-26
(20, 3, '2024-06-25', '1818-01-01');  -- Frankenstein - 3rd Edition - Added: 2024-06-25, Written: 1818-01-01



-- Inserting data into StockQuantity table
INSERT INTO StockQuantity (isbn_id, number_of_books, book_type) VALUES
(1, 9, 'Paperback'),  -- The Great Gatsby - ISBN: 1, Paperback - Quantity: 100
(2, 120, 'Hardcover'),  -- To Kill a Mockingbird - ISBN: 2, Hardcover - Quantity: 120
(3, 90, 'Paperback'),   -- 1984 - ISBN: 3, Paperback - Quantity: 90
(4, 80, 'Paperback'),   -- Pride and Prejudice - ISBN: 4, Paperback - Quantity: 80
(5, 110, 'Hardcover'),  -- The Catcher in the Rye - ISBN: 5, Hardcover - Quantity: 110
(6, 70, 'Paperback'),   -- Brave New World - ISBN: 6, Paperback - Quantity: 70
(7, 85, 'Hardcover'),   -- To the Lighthouse - ISBN: 7, Hardcover - Quantity: 85
(8, 95, 'Paperback'),   -- Animal Farm - ISBN: 8, Paperback - Quantity: 95
(9, 150, 'Hardcover'),  -- The Lord of the Rings - ISBN: 9, Hardcover - Quantity: 150
(10, 130, 'Paperback'), -- The Hobbit - ISBN: 10, Paperback - Quantity: 130
(11, 180, 'Hardcover'), -- Harry Potter and the Philosopher's Stone - ISBN: 11, Hardcover - Quantity: 180
(12, 8, 'Paperback'),  -- Moby-Dick - ISBN: 12, Paperback - Quantity: 75
(13, 110, 'Hardcover'), -- Ulysses - ISBN: 13, Hardcover - Quantity: 110
(14, 95, 'Paperback'),  -- The Odyssey - ISBN: 14, Paperback - Quantity: 95
(15, 100, 'Hardcover'), -- Don Quixote - ISBN: 15, Hardcover - Quantity: 100
(16, 120, 'Paperback'), -- War and Peace - ISBN: 16, Paperback - Quantity: 120
(17, 80, 'Paperback'),  -- The Brothers Karamazov - ISBN: 17, Paperback - Quantity: 80
(18, 90, 'Hardcover'),  -- The Picture of Dorian Gray - ISBN: 18, Hardcover - Quantity: 90
(19, 2, 'Paperback'),  -- Alice's Adventures in Wonderland - ISBN: 19, Paperback - Quantity: 85
(20, 100, 'Hardcover'); -- Frankenstein - ISBN: 20, Hardcover - Quantity: 100
