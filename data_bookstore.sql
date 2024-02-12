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
