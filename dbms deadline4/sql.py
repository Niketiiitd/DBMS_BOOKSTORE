import mysql.connector

mydb = mysql.connector.connect(
    host="Nikets-MacBook-Air.local",
    user="root",
    password="Niket@mac",
    database="bookshop", 
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()


def check_cart_availability(cursor, cart_items):
    unavailable_books = []
    for item in cart_items:
        book_id = item[0]
        quantity = item[2]

        # Check if the requested quantity is available
        cursor.execute("SELECT book_title, book_availability FROM Book WHERE book_id = %s", (book_id,))
        book_info = cursor.fetchone()
        
        if book_info[1] < quantity:
            unavailable_books.append((book_info[0], quantity, book_info[1]))

    return unavailable_books



def customer_signup():
    print("Customer Signup")
    name = input("Enter your name: ")

    # Validate house number input
    while True:
        try:
            house_no = int(input("Enter your house number: "))
            break
        except ValueError:
            print("Please enter a valid house number (numeric value).")

    street_name = input("Enter your street name: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zip_code = input("Enter your ZIP code: ")

    # Validate ZIP code input
    while True:
        try:
            zip_code = int(zip_code)
            break
        except ValueError:
            print("Please enter a valid ZIP code (numeric value).")
            zip_code = input("Enter your ZIP code: ")

    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Validate age input
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid age (numeric value).")

    try:
        cursor.execute("INSERT INTO Address (House_NO, Street_Name, City, State, Zip) VALUES (%s, %s, %s, %s, %s)",
                       (house_no, street_name, city, state, zip_code))
        mydb.commit()

        address_id = cursor.lastrowid

        cursor.execute("INSERT INTO Customer (customer_name, Address_ID, phone_number, email, customer_password, age) VALUES (%s, %s, %s, %s, %s, %s)",
                       (name, address_id, phone_number, email, password, age))
        mydb.commit()

        print("Customer signup successful!")
    except mysql.connector.Error as err:
        print("Error:", err)

def vendor_signup():
    print("Vendor Signup")
    name = input("Enter vendor name: ")
    email = input("Enter email: ")
    vend_password = input("Enter your password")
    
    # Validate age input
    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Please enter a valid age (numeric value).")

    phone_number = input("Enter phone number: ")
    
    # Validate phone number input
    while True:
        try:
            phone_number = int(phone_number)
            break
        except ValueError:
            print("Please enter a valid phone number (numeric value).")
            phone_number = input("Enter phone number: ")
    
    try:
        cursor.execute("INSERT INTO Vendor (vendor_name, Email, Age, Phone_number, vendor_password) VALUES (%s, %s, %s, %s, %s)",
                       (name, email, age, phone_number, vend_password))
        mydb.commit()
        print("Vendor signup successful!")
    except mysql.connector.Error as err:
        print("Error:", err)


def delivery_agent_signup():
    print("Delivery Agent Signup")
    name = input("Enter delivery agent name: ")
    password = input("Enter password: ")
    availability = input("Enter availability (Available/Unavailable): ")
    phone_number = input("Enter phone number: ")
    
    # Validate phone number input
    while True:
        try:
            phone_number = int(phone_number)
            break
        except ValueError:
            print("Please enter a valid phone number (numeric value).")
            phone_number = input("Enter phone number: ")
    
    try:
        cursor.execute("INSERT INTO DeliveryAgent (da_name, da_password, availability, da_phone_no) VALUES (%s, %s, %s, %s)",
                       (name, password, availability, phone_number))
        mydb.commit()
        print("Delivery agent signup successful!")
    except mysql.connector.Error as err:
        print("Error:", err)


def admin_signup():
    print("Admin Signup")
    admin_id = input("Enter admin ID: ")
    password = input("Enter password: ")
    
    # Validate admin ID input
    while True:
        try:
            admin_id = int(admin_id)
            break
        except ValueError:
            print("Please enter a valid admin ID (numeric value).")
            admin_id = input("Enter admin ID: ")
    
    try:
        cursor.execute("INSERT INTO MAIN_ADMIN (adminID, hashed_password) VALUES (%s, %s)",
                       (admin_id, password))
        mydb.commit()
        print("Admin signup successful!")
    except mysql.connector.Error as err:
        print("Error:", err)


# Signup function
def signup():
    while True:
        print("\nSignup as:")
        print("1. Customer")
        print("2. Vendor")
        print("3. Delivery Agent")
        print("4. Admin")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            customer_signup()
        elif choice == 2:
            vendor_signup()
        elif choice == 3:
            delivery_agent_signup()
        elif choice == 4:
            admin_signup()
        elif choice == 5:
            print("Exiting signup...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    homepage()


def login():
    while True:
        print("Enter as:")
        print("1.Customer")
        print("2.Vendor")
        print("3.Delivery Agent")
        print("4.Admin")
        print("5.Exit")
        print("Enter your Choice:", end=" ")
        choice = int(input())
        
        if choice == 1:
            cust_number = input("Enter Customer Phone number: ")

            if len(cust_number) != 10:
                print("Incorrect length of phone number. Please enter a 10-digit phone number.")
                continue
            
            # Check if the account is banned
            cursor.execute("SELECT is_banned FROM Customer WHERE phone_number = %s", (cust_number,))
            is_banned_result = cursor.fetchone()
            
            if is_banned_result and is_banned_result[0]:  # If the account is banned
                print("Your account has been suspended! Please contact admin to continue.")
                continue  # Skip login attempt
                
            cust_pass = input("Enter Customer Password: ")
            # Counter for incorrect password attempts
            incorrect_attempts = 0
            
            # Execute SQL query to check if customer exists
            cursor.execute("SELECT customer_password, incorrect_attempts FROM Customer WHERE phone_number = %s", (cust_number,))
            result = cursor.fetchone()
            
            if result:
                db_cust_pass, db_incorrect_attempts = result  # Fetch the password and incorrect attempts from the database
                while cust_pass != db_cust_pass:
                    incorrect_attempts += 1
                    if incorrect_attempts >= 3:
                        print("Too many incorrect attempts. Your account has been suspended! Please contact admin to continue.")
                        # Logic to ban the account in the database
                        cursor.execute("UPDATE Customer SET is_banned = 1 WHERE phone_number = %s", (cust_number,))
                        # connection.commit()
                        break
                    print("Wrong Password! Please try again.")
                    cust_pass = input("Enter Customer Password: ")
                
                # Update the incorrect attempts in the database
                new_incorrect_attempts = db_incorrect_attempts + incorrect_attempts
                cursor.execute("UPDATE Customer SET incorrect_attempts = %s WHERE phone_number = %s", (new_incorrect_attempts, cust_number))
                # connection.commit()
                
                if incorrect_attempts < 3:
                    print("Customer Login Successful!")
                    cursor.execute("UPDATE Customer SET incorrect_attempts = 0 WHERE phone_number = %s", (cust_number,))
                    CustomerCommands(cust_number)
            else:
                print("No such customer found!")

        elif choice == 2:
            # Vendor login
            vendor_phone_number = input("Enter Vendor Phone number: ")

            if len(vendor_phone_number)!=10:
                print("Incorrect length of phone number. Please enter a 10-digit phone number.")
                continue

                # Check if the account is banned
            cursor.execute("SELECT vendor_banned FROM Vendor WHERE Phone_number = %s", (vendor_phone_number,))
            vendor_banned_result = cursor.fetchone()
            
            if vendor_banned_result and vendor_banned_result[0]:  # If the account is banned
                print("Your account has been suspended! Please contact admin to continue.")
                continue  # Skip login attempt
                
            vendor_pass = input("Enter Vendor Password: ")
            # Counter for incorrect password attempts
            vendor_incorrect_attempts = 0
            
            # Execute SQL query to check if vendor exists
            cursor.execute("SELECT vendor_password, vendor_incorrect_attempts FROM Vendor WHERE Phone_number = %s", (vendor_phone_number,))
            v_result = cursor.fetchone()
            
            if v_result:
                db_vendor_pass, db_vendor_attempts = v_result  # Fetch the password and incorrect attempts from the database
                while vendor_pass != db_vendor_pass:
                    vendor_incorrect_attempts += 1
                    if vendor_incorrect_attempts >= 3:
                        print("Too many incorrect attempts. Your account has been suspended! Please contact admin to continue.")
                        # Logic to ban the account in the database
                        cursor.execute("UPDATE Vendor SET vendor_banned = 1 WHERE Phone_number = %s", (vendor_phone_number,))
                        # connection.commit()
                        break
                    print("Wrong Password! Please try again.")
                    vendor_pass = input("Enter Vendor Password: ")
                
                # Update the incorrect attempts in the database
                new_vendor_attempts = db_vendor_attempts + vendor_incorrect_attempts
                cursor.execute("UPDATE Vendor SET vendor_incorrect_attempts = %s WHERE Phone_number = %s", (new_vendor_attempts, vendor_phone_number))
                # connection.commit()
                
                if vendor_incorrect_attempts < 3:
                    print("Vendor Login Successful!")
                    cursor.execute("UPDATE Vendor SET vendor_incorrect_attempts = 0 WHERE Phone_number = %s", (vendor_phone_number,))
                    VendorCommands(vendor_phone_number)
            else:
                print("No such vendor found!")
        
        elif choice == 3:
            # Delivery Agent login
            da_name = input("Enter Delivery Agent Name: ")
            da_pass = input("Enter Delivery Agent Password: ")
            
            # Execute SQL query to check if delivery agent exists
            cursor.execute("SELECT da_name FROM DeliveryAgent WHERE da_name = %s AND da_password = %s", (da_name, da_pass))
            result = cursor.fetchone()
            
            if result:
                print("Delivery Agent Login Successful!")
                DeliveryAgentCommands()
                # Additional logic for delivery agent login can be added here
            else:
                print("No such delivery agent found!")
        
        elif choice == 4:
            # Admin login
            admin_id = int(input("Enter Admin ID: "))
            admin_pass = input("Enter Admin Password: ")
            
            # Execute SQL query to check if admin exists
            cursor.execute("SELECT hashed_password FROM MAIN_ADMIN WHERE adminID = %s", (admin_id,))
            result = cursor.fetchone()
            
            if result:
                db_admin_pass = result[0]  # Fetch the hashed password from the database
                if db_admin_pass == admin_pass:
                    print("Admin Login Successful!")
                    AdminCommands()
                    # Additional logic for admin login can be added here
                else:
                    print("Wrong Password!")
            else:
                print("No such admin found!")
        
        elif choice == 5:
            
            break
    homepage()
    

def CustomerCommands(customer_number):
    
    while (True):
        cursor.execute("SELECT customer_id FROM Customer WHERE phone_number = %s", (customer_number,))
        result1 = cursor.fetchone()
        cust_id = result1[0]
        print("1. View Books")
        print("2. Search")
        print("3. Add books to cart")
        print("4. Show order history")
        print("5. Show Cart")
        print("6. Show your personal details")
        print("7. Show book reviews given by you")
        print("8. Show DA_Agent reviews given by you")
        print("9. Place order")
        print("10. Clear current cart ")
        print("11. Logout")
        
        # Prompt user for choice
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Execute SQL query to fetch all books
            cursor.execute("SELECT * FROM Book")
            books = cursor.fetchall()
            
            # Display fetched books
            if books:
                print("All Books:")
                for book in books:
                    print("Book ID:", book[0])
                    print("Title:", book[1])
                    print("Author:", book[2])
                    print("Genre:", book[3])
                    print("Series:", book[4])
                    print("Publication:", book[5])
                    print("Availability:", book[6])
                    print("Vendor ID:", book[7])
                    print("Price:", book[8])
                    print()
            else:
                print("No books found in the database.")
        
        # Add logic for other choices as needed
        elif choice == 2:
            # Search logic
            search_filters = {}
            
            # Ask user for search filters
            book_id = input("Enter Book ID (press Enter to skip): ")
            if book_id:
                search_filters['book_id'] = book_id
            
            title = input("Enter Title (press Enter to skip): ")
            if title:
                search_filters['book_title'] = title  # Corrected column name
                
            author = input("Enter Author (press Enter to skip): ")
            if author:
                search_filters['book_author'] = author  # Corrected column name
                
            genre = input("Enter Genre (press Enter to skip): ")
            if genre:
                search_filters['book_genre'] = genre
            
            series = input("Enter Series (press Enter to skip): ")
            if series:
                search_filters['book_series'] = series
            
            publication = input("Enter Publication (press Enter to skip): ")
            if publication:
                search_filters['book_publication'] = publication
            
            availability = input("Enter Availability (press Enter to skip): ")
            if availability:
                search_filters['book_availability'] = availability
            
            vendor_id = input("Enter Vendor ID (press Enter to skip): ")
            if vendor_id:
                search_filters['VendorID'] = vendor_id  # Corrected column name
            
            price = input("Enter Price (press Enter to skip): ")
            if price:
                # Construct filter for price lower than entered
                search_filters['book_price'] = price   # Corrected column name and added comparison operator
                
            
            # Construct SQL query based on provided filters
            sql_query = "SELECT * FROM Book WHERE "
            conditions = []
            for key, value in search_filters.items():
                if key == 'book_price':
                    conditions.append(f"{key} < {value}")
                else:
                    
                    conditions.append(f"{key} = '{value}'")
            
            # Join conditions using 'OR' operator
            sql_query += " OR ".join(conditions)
            print(sql_query)
            # Execute SQL query
            cursor.execute(sql_query)
            search_results = cursor.fetchall()

            
            # Display search results
            if search_results:
                print("Search Results:")
                for book in search_results:
                    print("Book ID:", book[0])
                    print("Title:", book[1])
                    print("Author:", book[2])
                    print("Genre:", book[3])
                    print("Series:", book[4])
                    print("Publication:", book[5])
                    print("Availability:", book[6])
                    print("Vendor ID:", book[7])
                    print("Price:", book[8])
                    print()
            else:
                print("No books found matching the provided criteria.")
            
            # Add logic for other choices as needed
        elif choice == 3:
            # Fetch cart_id for the corresponding customer
            cursor.execute("SELECT cart_id FROM Cart WHERE customer_id = %s", (cust_id,))
            cart_info = cursor.fetchone()
            
            if cart_info:
                cart_id = cart_info[0]
                flag = 0
            else:
                flag = 1

            # Proceed with adding books to the cart
            book_id = input("Enter the Book ID you want to add to your cart: ")
            quantity = int(input("Enter the quantity: "))

            # Check if the book exists and is available
            cursor.execute("SELECT * FROM Book WHERE book_id = %s", (book_id,))
            book = cursor.fetchone()

            if book:
                # Check if the requested quantity is available
                if book[6] >= quantity:
                    # Check if the book already exists in the cart
                    cursor.execute("SELECT quantity FROM Cart WHERE customer_id = %s AND book_id = %s", (cust_id, book_id))
                    existing_quantity = cursor.fetchone()

                    if existing_quantity:
                        # If the book already exists in the cart, update its quantity
                        new_quantity = existing_quantity[0] + quantity
                        cursor.execute("UPDATE Cart SET quantity = %s WHERE customer_id = %s AND book_id = %s",
                                    (new_quantity, cust_id, book_id))
                    else:
                        # Otherwise, insert the book into the cart
                        if flag == 0:
                            cursor.execute("INSERT INTO Cart (cart_id, customer_id, book_id, quantity) VALUES (%s, %s, %s, %s)",
                                            (cart_id, cust_id, book_id, quantity))
                        else:
                            cursor.execute("INSERT INTO Cart (customer_id, book_id, quantity) VALUES (%s, %s, %s)",
                                            (cust_id, book_id, quantity))

                    mydb.commit()
                    print("Book added to cart successfully!")
                else:
                    print("Sorry, the requested quantity is not available.")
            else:
                print("Book not found.")

        elif choice == 4:
            cursor.execute("SELECT * FROM customer_order WHERE customer_id = %s", (cust_id,))
            orders = cursor.fetchall()

            if orders:
                print("Your Order History:")
                for order in orders:
                    order_id = order[0]
                    order_date = order[1]
                    total_price = order[3]
                    order_status = order[4]
                    address_id = order[5]
                    payment_mode = order[6]
                    
                    # Fetch address details from the Address table
                    cursor.execute("SELECT * FROM Address WHERE Address_ID = %s", (address_id,))
                    address_info = cursor.fetchone()
                    
                    if address_info:
                        house_no = address_info[1]
                        street_name = address_info[2]
                        city = address_info[3]
                        state = address_info[4]
                        zip_code = address_info[5]
                        
                        print("Order ID:", order_id)
                        print("Order date:", order_date)
                        print("Total Price:", total_price)
                        print("Order status:", order_status)
                        print("Address:")
                        print("House Number:", house_no)
                        print("Street Name:", street_name)
                        print("City:", city)
                        print("State:", state)
                        print("Zip Code:", zip_code)
                        print("Payment Mode:", payment_mode)
                        print()
                    else:
                        print("Address details not found for Order ID:", order_id)
            else:
                print("You haven't placed any orders yet.")

        elif choice == 5:
            # Cart logic
            cursor.execute("SELECT c.book_id, b.book_price, c.quantity FROM Cart c JOIN Book b ON c.book_id = b.book_id WHERE c.customer_id = %s", (cust_id,))
            cart_items = cursor.fetchall()

            if cart_items:
                total_value = 0
                print("Your Cart:")
                for item in cart_items:
                    book_id = item[0]
                    price = item[1]
                    quantity = item[2]
                    total_item_value = price * quantity
                    total_value += total_item_value
                    print("Book ID:", book_id)
                    print("Quantity:", quantity)
                    print("Item Value:", total_item_value)
                    print()
                print("Total Cart Value:", total_value)
            else:
                print("Your cart is empty.")

        elif choice == 6:
            # Personal details logic
            cursor.execute("SELECT * FROM Customer WHERE phone_number = %s", (customer_number,))
            user_info = cursor.fetchone()

            if user_info:
                print("Personal Information:")
                print("Customer ID:", user_info[0])
                print("Customer Name:", user_info[1])
                print("Address ID:", user_info[2])
                print("Phone Number:", user_info[3])
                print("Email:", user_info[4])
                print("Age:", user_info[6])
            else:
                print("User not found.")
            pass
        
        elif choice == 7:
                # Book reviews logic
                # Execute SQL query to fetch book reviews given by the customer
                cursor.execute("SELECT * FROM ProductReview WHERE customer_id = %s", (cust_id,))
                reviews = cursor.fetchall()

                if reviews:
                    print("Your Book Reviews:")
                    for review in reviews:
                        print("Review ID:", review[0])
                        print("Book ID:", review[1])
                        print("Rating:", review[3])
                        print("Content:", review[4])
                        print()
                else:
                    print("You haven't given any book reviews yet.")
        elif choice == 8:
            # DA Agent reviews logic
            cursor.execute("SELECT * FROM DAgentReview WHERE customer_id = %s", (cust_id,))
            da_agent_reviews = cursor.fetchall()

            if da_agent_reviews:
                print("Your Delivery Agent Reviews:")
                for review in da_agent_reviews:
                    review_id = review[0]
                    da_id = review[1]
                    agent_review = review[3]
                    agent_review_description = review[4]
                    agent_review_date = review[5]

                    print("Review ID:", review_id)
                    print("Agent Review out of 5:", agent_review)
                    print("Review Description:", agent_review_description)
                    print("Review Date:", agent_review_date)
                    print()
            else:
                print("You haven't given any delivery agent reviews yet.")

                
        elif choice == 9:
            # Place order logic
            unavailable_books = check_cart_availability(cursor, cart_items)
            if unavailable_books:
                print("The following books are not available in the selected quantity:")
                for book in unavailable_books:
                    print(f"Book: {book[0]}, Requested Quantity: {book[1]}, Available Quantity: {book[2]}")
                print("Please update your cart accordingly.")
            else:
                cursor.execute("SELECT * FROM Cart WHERE customer_id = %s", (cust_id,))
                cart_items = cursor.fetchall()

                if not cart_items:
                    print("Your cart is empty. Please add items to your cart before placing an order.")
                else:
                    # Display cart items
                    # print("Your Cart:")
                    cursor.execute("SELECT c.book_id, b.book_price, c.quantity FROM Cart c JOIN Book b ON c.book_id = b.book_id WHERE c.customer_id = %s", (cust_id,))
                    cart_items = cursor.fetchall()

                    if cart_items:
                        total_value = 0
                    
                        for item in cart_items:
                            book_id = item[0]
                            price = item[1]
                            quantity = item[2]
                            total_item_value = price * quantity
                            total_value += total_item_value
                    print("Total Cart Value:", total_value)
                    

                    # Ask for address and mode of payment
                address_choice = input("Do you want to use your saved address? (yes/no): ").lower()
                if address_choice == "yes":
                    # Retrieve and display saved address from Customer table
                    cursor.execute("SELECT Address_ID FROM Customer WHERE customer_id = %s", (cust_id,))
                    address_id = cursor.fetchone()[0]

                    cursor.execute("SELECT * FROM Address WHERE Address_ID = %s", (address_id,))
                    address_info = cursor.fetchone()

                    if address_info:
                        print("Your Saved Address:")
                        print("House Number:", address_info[1])
                        print("Street Name:", address_info[2])
                        print("City:", address_info[3])
                        print("State:", address_info[4])
                        print("Zip Code:", address_info[5])
                    else:
                        print("You haven't saved any address yet.")
                elif address_choice == "no":
                    # Ask for new address
                    house_no = int(input("Enter your house number: "))
                    street_name = input("Enter your street name (press Enter to skip): ")
                    city = input("Enter your city: ")
                    state = input("Enter your state: ")
                    zip_code = int(input("Enter your zip code: "))

                    # Insert new address into the Address table
                    cursor.execute("INSERT INTO Address (House_NO, Street_Name, City, State, Zip) VALUES (%s, %s, %s, %s, %s)",
                                (house_no, street_name, city, state, zip_code))
                    mydb.commit()

                    # Retrieve the address_id of the newly inserted address
                    address_id = cursor.lastrowid

                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")

                # Ask for mode of payment
                payment_mode = input("Enter mode of payment (e.g., Credit Card, PayPal, etc.): ")

                # Insert order into customer_order table
                cursor.execute("INSERT INTO customer_order (customer_id, total_price, address, payment_mode) VALUES (%s, %s, %s, %s)",
                            (cust_id, total_value, address_id, payment_mode))
                order_id = cursor.lastrowid

                # Inserting the items from the cart into the OrderItem table
                for item in cart_items:
                    for item in cart_items:
                        book_id = item[0]  # Index 0 corresponds to book_id
                        price = item[1]    # Index 1 corresponds to book_price
                        quantity = item[2] # Index 2 corresponds to quantity

                    cursor.execute("INSERT INTO OrderItem (book_id, order_id, quantity) VALUES (%s, %s, %s)",
                                (book_id, order_id, quantity))

                # Clear the cart after placing the order
                cursor.execute("DELETE FROM Cart WHERE customer_id = %s", (cust_id,))
                mydb.commit()

                print("Your order has been successfully placed. Thank you for shopping with us!")

        elif choice == 10:
            cursor.execute("DELETE FROM Cart WHERE customer_id = %s", (cust_id,))
            mydb.commit()
            print("Your cart has been cleared.")
        elif choice == 11:
            # Logout logic
            print("Signing out...")
            break
            
        else:
            print("Invalid choice. Please enter a valid option.")
    login()
    
def VendorCommands():
    while True:
        cursor.execute("SELECT vendor_id FROM Vendor WHERE phone_number = %s", (vendor_number,))
        vendor_id = cursor.fetchone()[0]  # Assuming phone_number uniquely identifies a vendor
        
        print("1. View Vendor Books")
        print("2. Search")
        print("3. Add book")
        print("4. Delete book")
        print("5. Edit book stock")
        print("6. Show your personal details")
        print("7. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            cursor.execute("SELECT * FROM Book WHERE VendorID = %s", (vendor_id,))
            books = cursor.fetchall()
            if books:
                print("All Books:")
                for book in books:
                    print("Book ID:", book[0])
                    print("Title:", book[1])
                    print("Author:", book[2])
                    print("Genre:", book[3])
                    print("Series:", book[4])
                    print("Publication:", book[5])
                    print("Availability:", book[6])
                    print("Price:", book[7])
                    print()
            else:
                print("No books found in the database.")
        
        elif choice == '2':
            # Search logic
            search_filters = {}
            
            # Ask user for search filters
            book_id = input("Enter Book ID (press Enter to skip): ")
            if book_id:
                search_filters['book_id'] = book_id
            
            title = input("Enter Title (press Enter to skip): ")
            if title:
                search_filters['book_title'] = title  # Corrected column name
                
            author = input("Enter Author (press Enter to skip): ")
            if author:
                search_filters['book_author'] = author  # Corrected column name
                
            genre = input("Enter Genre (press Enter to skip): ")
            if genre:
                search_filters['book_genre'] = genre
            
            series = input("Enter Series (press Enter to skip): ")
            if series:
                search_filters['book_series'] = series
            
            publication = input("Enter Publication (press Enter to skip): ")
            if publication:
                search_filters['book_publication'] = publication
            
            availability = input("Enter Availability (press Enter to skip): ")
            if availability:
                search_filters['book_availability'] = availability
            
            # vendor_id = input("Enter Vendor ID (press Enter to skip): ")
            # if vendor_id:
            #     search_filters['VendorID'] = vendor_id  # Corrected column name
            
            price = input("Enter Price (press Enter to skip): ")
            if price:
                # Construct filter for price lower than entered
                search_filters['book_price'] = price   # Corrected column name and added comparison operator
                
            
            # Construct SQL query based on provided filters
            sql_query = "SELECT * FROM Book JOIN Vendor ON Book.VendorID = Vendor.VendorID WHERE Vendor.VendorID = %s", (VendorID,)
            conditions = []
            for key, value in search_filters.items():
                if key == 'book_price':
                    conditions.append(f"{key} < {value}")
                else:
                    
                    conditions.append(f"{key} = '{value}'")
            
            # Join conditions using 'OR' operator
            sql_query += " OR ".join(conditions)
            print(sql_query)
            # Execute SQL query
            cursor.execute(sql_query)
            search_results = cursor.fetchall()

            
            # Display search results
            if search_results:
                print("Search Results:")
                for book in search_results:
                    print("Book ID:", book[0])
                    print("Title:", book[1])
                    print("Author:", book[2])
                    print("Genre:", book[3])
                    print("Series:", book[4])
                    print("Publication:", book[5])
                    print("Availability:", book[6])
                    print("Vendor ID:", book[7])
                    print("Price:", book[7])
                    print() 
            else:
                print("No books found matching the provided criteria.")
            
        elif choice == '3':
            # Add a book
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre: ")
            series = input("Enter Series: ")
            publication = input("Enter Publication: ")
            stock = int(input("Enter Availability: "))
            price = int(input("Enter Price: "))

            cursor.execute("INSERT INTO Book (book_title, book_author, book_genre, book_series, book_publication, book_availability, VendorID, book_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (title, author, genre, series, publication, stock, vendor_id, price))
            mydb.commit()

            print("Book added successfully")
        
        elif choice == '4':
            # Delete a book
            book_id_to_delete = int(input("Enter the ID of the book you want to delete: "))
            cursor.execute("SELECT * FROM Book WHERE book_id = %s AND VendorID = %s", (book_id_to_delete, vendor_id))
            book = cursor.fetchone()
            if book:
                cursor.execute("DELETE FROM Book WHERE book_id = %s", (book_id_to_delete,))
                mydb.commit()
                print("Book deleted successfully.")
            else:
                print("Invalid Book ID or book belongs to another vendor.")
            
        elif choice == '5':
            # Edit book stock
            book_id_to_edit = int(input("Enter the ID of the book you want to edit: "))
            new_stock = int(input("Enter the new stock for the book: "))
            cursor.execute("SELECT * FROM Book WHERE book_id = %s AND VendorID = %s", (book_id_to_edit, vendor_id))
            book = cursor.fetchone()
            if book:
                cursor.execute("UPDATE Book SET book_availability = %s WHERE book_id = %s", (new_stock, book_id_to_edit))
                mydb.commit()
                print("Book stock updated successfully.")
            else:
                print("Invalid Book ID or  book belongs to another vendor.")
        
       
            
        elif choice == '6':
            # Show vendor's personal details
            cursor.execute("SELECT * FROM Vendor WHERE vendor_id = %s", (vendor_id,))
            vendor_info = cursor.fetchone()
            if vendor_info:
                print("Personal Information:")
                print("Vendor ID:", vendor_info[0])
                print("Vendor Name:", vendor_info[1])
                print("Email:", vendor_info[2])
                print("Age:", vendor_info[3])
                print("Phone Number:", vendor_info[4])

            else:
                print("Vendor not found.")
        
        elif choice == '7':
            print("Logging out...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")
    
    login()
    
def DeliveryAgentCommands():
    while True:
        try:
            agent_id = int(input("Enter Delivery Agent ID: "))
            cursor.execute("SELECT * FROM DeliveryAgent WHERE agent_id = %s", (agent_id,))
            agent = cursor.fetchone()

            if not agent:
                print("Delivery agent not found.")
                return
            
            print("Delivery Agent Commands:")
            print("1. Personal Details")
            print("2. Availability")
            print("3. Area Servicing")
            print("4. Orders: Current")
            print("5. Orders: Past")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                cursor.execute("SELECT * FROM DeliveryAgent WHERE daID = %s", (agent_id,))
                agent_info = cursor.fetchone()
                if agent_info:
                    print("Personal Information:")
                    print("Vendor ID:", agent_info[0])
                    print("Vendor Name:", agent_info[1])
                    #print("Email:", vendor_info[2])
                    print("Availability:", agent_info[3])
                    print("Phone Number:", agent_info[4])

                else:
                    print("Vendor not found.")
            
            elif choice == '2':
                availability = input("Enter your availability (e.g., 'Available' or 'Unavailable'): ")
                cursor.execute("UPDATE DeliveryAgent SET availability = %s WHERE agent_id = %s", (availability, agent_id))
                mydb.commit() 
                print("Availability updated successfully.")

            elif choice == '3':
                area_servicing = input("Enter the area you are servicing: ")
                
                # Add the area_servicing column to the DeliveryAgent table
                cursor.execute("ALTER TABLE DeliveryAgent ADD IF NOT EXISTS area_servicing VARCHAR(255)")
                
                # Update the area_servicing value for the specific agent
                cursor.execute("UPDATE DeliveryAgent SET area_servicing = %s WHERE agent_id = %s", (area_servicing, agent_id))
                mydb.commit()
                
                print("Area servicing updated successfully.")

            elif choice == '4':
                cursor.execute("SELECT * FROM Orders WHERE delivery_agent_id = %s AND delivery_status = 'In transit'", (agent_id,))
                current_orders = cursor.fetchall()
                print("Order ID",current_orders[0])
                print("Order Status",current_orders[1])
                print("Order Date",current_orders[2])
                print("Customer ID",current_orders[4])

            elif choice == '5':
                cursor.execute("SELECT * FROM Orders WHERE delivery_agent_id = %s AND (delivery_status = 'Delivered' OR delivery_status = 'Cancelled')", (agent_id,))
                past_orders= cursor.fetchall()
                print("Order ID", past_orders[0])
                print("Order Status",past_orders[1])
                print("Order Date",past_orders[2])
                print("Customer ID",past_orders[4])

            elif choice == '6':
                print("Logging out...")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
def AdminCommands():
    print("hello")

# login()

def homepage():
    while True:
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        choice = int(input("Enter your choice: "))
            
        if choice == 1:
            signup()
        elif choice==2:
            login()
        elif choice==3:
            break
        else:
            print("Invalid choice. Please enter a valid option.")
homepage()   

# def print_all_vendors():
#     # Execute SQL query to fetch all vendors
#     cursor.execute("SELECT * FROM Vendor")
#     vendors = cursor.fetchall()
    
#     # Print all vendors
#     for vendor in vendors:
#         print(vendor)
# print_all_vendors()
