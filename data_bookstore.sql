use bookstore_dbms;


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
('Oliver', 'oliver@example.com', 35, 1234567890),
('June', 'june@example.com', 40, 2345678901),
('Agust', 'agust@example.com', 45, 3456789012),
('Sophia', 'sophia@example.com', 50, 4567890123),
('Ethan', 'ethan@example.com', 55, 5678901234),
('Emma', 'emma@example.com', 60, 6789012345),
('Mia', 'mia@example.com', 65, 7890123456),
('James', 'james@example.com', 70, 8901234567),
('Ava', 'ava@example.com', 75, 9012345678),
('William', 'william@example.com', 80, 1234567890),
('Olivia', 'olivia@example.com', 85, 2345678901),
('Isaac', 'isaac@example.com', 90, 3456789012),
('Charlotte', 'charlotte@example.com', 95, 4567890123),
('Amelia', 'amelia@example.com', 100, 5678901234),
('Michael', 'michael@example.com', 105, 6789012345),
('Emma', 'emma2@example.com', 110, 7890123456),
('Jacob', 'jacob@example.com', 115, 8901234567),
('Abigail', 'abigail@example.com', 120, 9012345678),
('Elijah', 'elijah@example.com', 125, 1234567890),
('Sophia', 'sophia2@example.com', 130, 2345678901);


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
INSERT INTO Customer (customer_name, Address_ID, phone_number, email, customer_password) VALUES
('John Doe', 1, 1234567890, 'john@example.com', 'password1'),
('Jane Smith', 2, 2345678901, 'jane@example.com', 'password2'),
('Michael Johnson', 3, 3456789012, 'michael@example.com', 'password3'),
('Emily Davis', 4, 4567890123, 'emily@example.com', 'password4'),
('Christopher Wilson', 5, 5678901234, 'christopher@example.com', 'password5'),
('Amanda Martinez', 6, 6789012345, 'amanda@example.com', 'password6'),
('David Anderson', 7, 7890123456, 'david@example.com', 'password7'),
('Jessica Taylor', 8, 8901234567, 'jessica@example.com', 'password8'),
('James Brown', 9, 9012345678, 'james@example.com', 'password9'),
('Sarah Thomas', 10, 1234567890, 'sarah@example.com', 'password10'),
('Matthew White', 11, 2345678901, 'matthew@example.com', 'password11'),
('Jennifer Lee', 12, 3456789012, 'jennifer@example.com', 'password12'),
('Daniel Harris', 13, 4567890123, 'daniel@example.com', 'password13'),
('Elizabeth Clark', 14, 5678901234, 'elizabeth@example.com', 'password14'),
('Christopher Martinez', 15, 6789012345, 'christopher2@example.com', 'password15'),
('Linda Lewis', 16, 7890123456, 'linda@example.com', 'password16'),
('Thomas Robinson', 17, 8901234567, 'thomas@example.com', 'password17'),
('Patricia Walker', 18, 9012345678, 'patricia@example.com', 'password18'),
('Matthew Hall', 19, 1234567890, 'matthew2@example.com', 'password19'),
('Karen Young', 20, 2345678901, 'karen@example.com', 'password20');

--Insert Values in DeliveryAgent Table
INSERT INTO DeliveryAgent (name,da_password,availability,da_phone_no)
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

--Insert Values in Warehouse Table
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

--Inserting Values in Orders Table
INSERT INTO Orders (Order_status, orderDATE, totalPrice)
VALUES
('Completed', '2024-02-01', 100),
('Pending', '2024-02-02', 150),
('Shipped', '2024-02-03', 120),
('Completed', '2024-02-04', 200),
('Pending', '2024-02-05', 180),
('Shipped', '2024-02-06', 250),
('Completed', '2024-02-07', 300),
('Pending', '2024-02-08', 220),
('Shipped', '2024-02-09', 280),
('Completed', '2024-02-10', 320);

--Inserting Values in ProductReviews Table
INSERT INTO ProductReview (book_id, rating, content)
VALUES
(1, 5, 'Great book! Highly recommended.'),
(2, 4, 'Interesting read, but could be better.'),
(3, 5, 'Absolutely loved it! Must-read for everyone.'),
(1, 3, 'Decent book, but not exceptional.'),
(2, 5, 'One of the best books I have ever read!'),
(3, 4, 'Well-written and thought-provoking.'),
(1, 4, 'Enjoyed reading it, would recommend.'),
(2, 3, 'Good book, but not my favorite.'),
(3, 5, 'Couldn''t put it down! Amazing story.'),
(1, 5, 'Incredible! Changed my perspective.');

--Inserting Values in Main_Admin Table
INSERT INTO MAIN_ADMIN (adminID, hashed_password)
VALUES
(1, 'admin1'),
(2, 'admin2'),
(3, 'admin3'),
(4, 'admin4');

--Inserting Values in Cart Table
INSERT INTO Cart (cart_price, customer_id, book_id)
VALUES
(150, 1, 1),
(200, 2, 2),
(180, 3, 3),
(220, 1, 4),
(250, 2, 5),
(300, 3, 6),
(280, 1, 7),
(320, 2, 8),
(350, 3, 9),
(380, 1, 10);

--Inserting Values in DAgentReview
INSERT INTO DAgentReview (daID, agent_review, agent_review_description, agent_review_date)
VALUES
(1, 4, 'Professional service, timely delivery.', '2024-02-01'),
(2, 5, 'Excellent service, highly recommended.', '2024-02-02'),
(3, 3, 'Average service, could improve communication.', '2024-02-03'),
(1, 4, 'Polite and helpful delivery agent.', '2024-02-04'),
(2, 5, 'Friendly and efficient delivery, thank you!', '2024-02-05'),
(3, 2, 'Late delivery, needs improvement.', '2024-02-06'),
(1, 5, 'Great service overall, no complaints.', '2024-02-07'),
(2, 4, 'Good communication and prompt delivery.', '2024-02-08'),
(3, 3, 'Delivery agent was rude and unprofessional.', '2024-02-09'),
(1, 5, 'Best delivery experience so far!', '2024-02-10');

--Insering Values in BookDescription Table
INSERT INTO BookDescription (book_id, book_description)
VALUES
(1, 'A gripping tale of love and loss set in a post-apocalyptic world.'),
(2, 'A fantasy epic filled with magic, dragons, and adventure.'),
(3, 'An insightful exploration of the human condition through the eyes of a young protagonist.'),
(4, 'A historical novel set during the French Revolution, filled with intrigue and romance.'),
(5, 'A science fiction masterpiece that challenges perceptions of reality and identity.'),
(6, 'A heartwarming story of friendship and courage in the face of adversity.'),
(7, 'A thrilling mystery set in Victorian London, with twists and turns at every corner.'),
(8, 'An exploration of race, identity, and society in contemporary America.'),
(9, 'A poetic journey through the landscapes of memory and longing.'),
(10, 'An inspiring tale of redemption and forgiveness in a small town.'),
(11, 'A gripping thriller that keeps you on the edge of your seat until the very end.'),
(12, 'A heart-wrenching story of love and sacrifice in wartime.'),
(13, 'An exploration of family dynamics and secrets in a small town.'),
(14, 'A dystopian adventure set in a society where books are forbidden.'),
(15, 'A whimsical journey through a magical realm filled with talking animals and enchantments.'),
(16, 'A psychological thriller that delves into the depths of the human mind.'),
(17, 'A coming-of-age tale set against the backdrop of the Civil Rights Movement.'),
(18, 'An epic quest to save the kingdom from darkness and despair.'),
(19, 'A contemporary romance that explores the complexities of modern relationships.'),
(20, 'A collection of short stories that spans genres and themes, showcasing the diversity of human experience.');

--Inserting Values in OrderItem table
INSERT INTO OrderItem (book_id, orderID, quantity)
VALUES
(1, 1, 2),
(2, 1, 1),
(3, 2, 3),
(4, 2, 1),
(5, 3, 2),
(6, 3, 1),
(7, 4, 2),
(8, 4, 1),
(9, 5, 3),
(10, 5, 2);

--Inserting values in ISBNInfo table
INSERT INTO ISBNInfo (book_id, edition, date_added, date_written)
VALUES
(1, 1, '2023-01-15', '2022-12-01'),
(2, 2, '2023-02-20', '2023-01-01'),
(3, 1, '2023-03-25', '2023-02-15'),
(4, 3, '2023-04-30', '2023-03-10'),
(5, 1, '2023-05-05', '2023-04-20'),
(6, 2, '2023-06-10', '2023-05-01'),
(7, 1, '2023-07-15', '2023-06-05'),
(8, 1, '2023-08-20', '2023-07-15'),
(9, 2, '2023-09-25', '2023-08-01'),
(10, 1, '2023-10-30', '2023-09-15'),
(11, 1, '2023-11-05', '2023-10-20'),
(12, 2, '2023-12-10', '2023-11-01'),
(13, 1, '2024-01-15', '2023-12-05'),
(14, 3, '2024-02-20', '2024-01-01'),
(15, 1, '2024-03-25', '2024-02-15'),
(16, 2, '2024-04-30', '2024-03-10'),
(17, 1, '2024-05-05', '2024-04-20'),
(18, 1, '2024-06-10', '2024-05-01'),
(19, 2, '2024-07-15', '2024-06-05'),
(20, 1, '2024-08-20', '2024-07-15');

--Inserting Values in StockQuantity Table
INSERT INTO StockQuantity (isbn_id, number_of_books, book_type)
VALUES
(1, 100, 'hardcopy'),
(2, 150, 'specialedition'),
(3, 120, 'ebook'),
(4, 200, 'hardcopy'),
(5, 180, 'specialedition'),
(6, 90, 'ebook'),
(7, 300, 'hardcopy'),
(8, 250, 'hardcopy'),
(9, 130, 'ebook'),
(10, 220, 'specialedition');
