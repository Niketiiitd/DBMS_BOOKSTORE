import mysql.connector
import threading
from flask import Flask, request, jsonify
mydb = mysql.connector.connect(
    host="Nikets-MacBook-Air.local",
    user="root",
    password="Niket@mac",
    database="bookshop", 
    auth_plugin='mysql_native_password'
)


cursor = mydb.cursor()


def change_customer_password(cust_number):
    print("Enter OTP")
    print("OTP Entered correctly.....")
    print()
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")
    
    if new_password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    

    try:
        cursor.execute("START TRANSACTION")
        

        cursor.execute("UPDATE Customer SET customer_password = %s WHERE phone_number = %s", (new_password, cust_number))
        
      
        mydb.commit()
        
        print("Password changed successfully!")
    
    except Exception as e:

        print("An error occurred:", str(e))
        print("Rolling back changes...")
        mydb.rollback()
    
    


# def display_message_from_trigger(cursor):

#     cursor.execute("SELECT message FROM LoginAttempts WHERE message IS NOT NULL")
#     result = cursor.fetchone()
#     if result:
#         print("Message from trigger:", result[0])
#     else:
#         print("No message from trigger.")

def customer_signup():
    print("Customer Signup")
    name = input("Enter your name: ")

 
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


    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid age (numeric value).")

    try:

        cursor.execute("START TRANSACTION")


        cursor.execute("INSERT INTO Address (House_NO, Street_Name, City, State, Zip) VALUES (%s, %s, %s, %s, %s)",
                       (house_no, street_name, city, state, zip_code))
        address_id = cursor.lastrowid

        
        cursor.execute("INSERT INTO Customer (customer_name, Address_ID, phone_number, email, customer_password, age) VALUES (%s, %s, %s, %s, %s, %s)",
                       (name, address_id, phone_number, email, password, age))

        mydb.commit()
        
        print("Customer signup successful!")
    except mysql.connector.Error as err:
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()

def vendor_signup():
    print("Vendor Signup")
    name = input("Enter vendor name: ")
    email = input("Enter email: ")
    vend_password = input("Enter your password: ")
    
    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Please enter a valid age (numeric value).")

    phone_number = input("Enter phone number: ")
    
    while True:
        try:
            phone_number = int(phone_number)
            break
        except ValueError:
            print("Please enter a valid phone number (numeric value).")
            phone_number = input("Enter phone number: ")
    
    try:
        cursor.execute("START TRANSACTION")
        
        cursor.execute("INSERT INTO Vendor (vendor_name, Email, Age, Phone_number, vendor_password) VALUES (%s, %s, %s, %s, %s)",
                       (name, email, age, phone_number, vend_password))
        
        mydb.commit()
        
        print("Vendor signup successful!")
    except mysql.connector.Error as err:
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()


def delivery_agent_signup():
    print("Delivery Agent Signup")
    name = input("Enter delivery agent name: ")
    password = input("Enter password: ")
    availability = input("Enter availability (Available/Unavailable): ").capitalize()  
    phone_number = input("Enter phone number: ")
    
    while True:
        try:
            phone_number = int(phone_number)
            break
        except ValueError:
            print("Please enter a valid phone number (numeric value).")
            phone_number = input("Enter phone number: ")
    
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        
        cursor.execute("INSERT INTO DeliveryAgent (da_name, da_password, availability, da_phone_no) VALUES (%s, %s, %s, %s)",
                       (name, password, availability, phone_number))
        
        # Commit transaction
        mydb.commit()
        
        print("Delivery agent signup successful!")
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()

def admin_signup():
    print("Admin Signup")
    admin_id = input("Enter admin ID: ")
    password = input("Enter password: ")
    

    while True:
        try:
            admin_id = int(admin_id)
            break
        except ValueError:
            print("Please enter a valid admin ID (numeric value).")
            admin_id = input("Enter admin ID: ")
    
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        # Insert admin
        cursor.execute("INSERT INTO MAIN_ADMIN (adminID, hashed_password) VALUES (%s, %s)",
                       (admin_id, password))
        
        # Commit transaction
        mydb.commit()
        
        print("Admin signup successful!")
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()


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
        # trigger 2 message
        # cursor.execute("SELECT * FROM order_summary")

        # # Fetch all rows from the result set
        # order_summary = cursor.fetchall()

        # # Print the order_summary table
        # for order in order_summary:
        #     print(order)

        # trigger 1 message
        # print("Blocked user here ---->")
        # cursor.execute("SELECT * FROM LoginAttempts")

        # # Fetch all rows from the result set
        # login_attempts = cursor.fetchall()

        # # Print the login attempts entries
        # for attempt in login_attempts:
            
        #     print(attempt)

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

            cursor.execute("SELECT is_banned FROM Customer WHERE phone_number = %s", (cust_number,))
            is_banned_result = cursor.fetchone()
            
            if is_banned_result and is_banned_result[0]: 
                print("Your account has been suspended! Please contact admin to continue.")
                continue  
            cust_pass = input("Enter Customer Password: ")
            flag_change_pass=0
            
            while True:
                
                

                cursor.execute("SELECT customer_password, incorrect_attempts FROM Customer WHERE phone_number = %s", (cust_number,))
                result = cursor.fetchone()
                
                if result:
                    db_cust_pass, db_incorrect_attempts = result  
                    incorrect_attempts = 0 
                    
                    while cust_pass != db_cust_pass:
                        incorrect_attempts += 1
                        if incorrect_attempts >= 3:
                            print("Too many incorrect attempts. Your account has been suspended! Please contact admin to continue.")
                            cursor.execute("UPDATE Customer SET is_banned = 1, incorrect_attempts = 0 WHERE phone_number = %s", (cust_number,))
                            mydb.commit() 
                            break
                        print("Wrong Password! Please try again.")
                        print("Change Password?")
                        change_option = input("Enter Y to change password or any other key to proceed: ").upper()
                        if change_option == "Y":
                            change_customer_password(cust_number)
                            flag_change_pass=1
                            break
                        cust_pass = input("Enter Customer Password: ")
                    if flag_change_pass == 1:
                        break
                    if incorrect_attempts >= 3:
                        cursor.execute("INSERT INTO LoginAttempts (message) VALUES (%s)", (cust_number,))
                        mydb.commit() 
                        break  
                    
                    if cust_pass == db_cust_pass:
                        print("Customer Login Successful!")
                        cursor.execute("UPDATE Customer SET incorrect_attempts = 0 WHERE phone_number = %s", (cust_number,))
                        CustomerCommands(cust_number)
                        break
                else:
                    print("No such customer found!")
        elif choice == 2:
           
            vendor_phone_number = input("Enter Vendor Phone number: ")

            if len(vendor_phone_number) != 10:
                print("Incorrect length of phone number. Please enter a 10-digit phone number.")
                continue

     
            cursor.execute("SELECT vendor_banned FROM Vendor WHERE Phone_number = %s", (vendor_phone_number,))
            vendor_banned_result = cursor.fetchone()

            if vendor_banned_result and vendor_banned_result[0]: 
                print("Your account has been suspended! Please contact admin to continue.")
                continue  

            vendor_pass = input("Enter Vendor Password: ")
            
            vendor_incorrect_attempts = 0

            
            cursor.execute("SELECT vendor_password, vendor_incorrect_attempts FROM Vendor WHERE Phone_number = %s", (vendor_phone_number,))
            v_result = cursor.fetchone()

            if v_result:
                db_vendor_pass, db_vendor_attempts = v_result  
                while vendor_pass != db_vendor_pass:
                    vendor_incorrect_attempts += 1
                    if vendor_incorrect_attempts >= 3:
                        print("Too many incorrect attempts. Your account has been suspended! Please contact admin to continue.")
                       
                        cursor.execute("UPDATE Vendor SET vendor_banned = 1 WHERE Phone_number = %s", (vendor_phone_number,))
                        mydb.commit()
                        break
                    print("Wrong Password! Please try again.")
                    vendor_pass = input("Enter Vendor Password: ")

                if vendor_incorrect_attempts < 3:
                    print("Vendor Login Successful!")
                    cursor.execute("UPDATE Vendor SET vendor_incorrect_attempts = 0 WHERE Phone_number = %s", (vendor_phone_number,))
                    mydb.commit()
                    VendorCommands(vendor_phone_number)
            else:
                print("No such vendor found!")

        elif choice == 3:
            
            da_name = input("Enter Delivery Agent Name: ")
            da_pass = input("Enter Delivery Agent Password: ")
            
            
            cursor.execute("SELECT da_name FROM DeliveryAgent WHERE da_name = %s AND da_password = %s", (da_name, da_pass))
            result = cursor.fetchone()
            
            if result:
                print("Delivery Agent Login Successful!")
                DeliveryAgentCommands()
                
            else:
                print("No such delivery agent found!")
        
        elif choice == 4:
            
            admin_id = int(input("Enter Admin ID: "))
            admin_pass = input("Enter Admin Password: ")
            
           
            cursor.execute("SELECT hashed_password FROM MAIN_ADMIN WHERE adminID = %s", (admin_id,))
            result = cursor.fetchone()
            
            if result:
                db_admin_pass = result[0]  
                if db_admin_pass == admin_pass:
                    print("Admin Login Successful!")
                    AdminCommands()
                    
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
        print("11. Know more about any book")
        print("12. Give book reviews")
        print("13. Logout")
        
        
        choice = int(input("Enter your choice: "))
     
        if choice == 1:
           
            cursor.execute("SELECT b.*, r.rating, r.content FROM Book b LEFT JOIN ProductReview r ON b.book_id = r.book_id")
            books_with_reviews = cursor.fetchall()
            
           
            if books_with_reviews:
                print("All Books:")
                for book in books_with_reviews:
                    print("Book ID:", book[0])
                    print("Title:", book[1])
                    print("Author:", book[2])
                    print("Genre:", book[3])
                    print("Series:", book[4])
                    print("Publication:", book[5])
                    print("Availability:", book[6])
                    print("Vendor ID:", book[7])
                    print("Price:", book[8])
                    print("Rating:", book[9])  
    
                    print()
            else:
                print("No books found in the database.")

      
        elif choice == 2:
            # Search logic
            search_filters = {}
            
          
            book_id = input("Enter Book ID (press Enter to skip): ")
            if book_id:
                search_filters['book_id'] = book_id
            
            title = input("Enter Title (press Enter to skip): ")
            if title:
                search_filters['book_title'] = title  
                
            author = input("Enter Author (press Enter to skip): ")
            if author:
                search_filters['book_author'] = author  
                
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
                search_filters['VendorID'] = vendor_id  
            
            price = input("Enter Price (press Enter to skip): ")
            if price:
             
                search_filters['book_price'] = price  
                
            
          
            sql_query = "SELECT * FROM Book WHERE "
            conditions = []
            for key, value in search_filters.items():
                if key == 'book_price':
                    conditions.append(f"{key} < {value}")
                else:
                    
                    conditions.append(f"{key} = '{value}'")
            
         
            sql_query += " OR ".join(conditions)
            print(sql_query)
            
            cursor.execute(sql_query)
            search_results = cursor.fetchall()

            
          
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
            
            
        elif choice == 3:
           
            cursor.execute("SELECT cart_id FROM Cart WHERE customer_id = %s", (cust_id,))
            cart_info = cursor.fetchone()
            
            if cart_info:
                cart_id = cart_info[0]
                flag = 0
            else:
                flag = 1

   
            book_id = input("Enter the Book ID you want to add to your cart: ")
            quantity = int(input("Enter the quantity: "))

           
            cursor.execute("SELECT * FROM Book WHERE book_id = %s", (book_id,))
            book = cursor.fetchone()

            if book:
                if book[6] >= quantity:
                    
                    cursor.execute("SELECT quantity FROM Cart WHERE customer_id = %s AND book_id = %s", (cust_id, book_id))
                    existing_quantity = cursor.fetchone()

                    if existing_quantity:
                       
                        new_quantity = existing_quantity[0] + quantity
                        cursor.execute("UPDATE Cart SET quantity = %s WHERE customer_id = %s AND book_id = %s",
                                    (new_quantity, cust_id, book_id))
                    else:
                       
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
                    print("Item Value:", price)
                    print()
                print("Total Cart Value:", total_value)
            else:
                print("Your cart is empty.")

        elif choice == 6:
           
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
            try:
                # Begin transaction
                cursor.execute("START TRANSACTION")
                
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
                
                # Commit transaction
                mydb.commit()
                print("Transaction successful!")
            
            except mysql.connector.Error as err:
                # Rollback transaction if any error occurs
                print("Error:", err)
                print("Rolling back changes...")
                mydb.rollback()

        elif choice == 8:
            
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
            
            cursor.execute("SELECT * FROM Cart WHERE customer_id = %s", (cust_id,))
            cart_items = cursor.fetchall()

            if not cart_items:
                print("Your cart is empty. Please add items to your cart before placing an order.")
                continue
            else:
                
                cursor.execute("SELECT c.book_id, b.book_price, c.quantity, b.book_availability FROM Cart c JOIN Book b ON c.book_id = b.book_id WHERE c.customer_id = %s", (cust_id,))
                cart_items = cursor.fetchall()

                if cart_items:
                    total_value = 0
                    can_place_order = True 

                    for item in cart_items:
                        book_id = item[0]
                        price = item[1]
                        quantity = item[2]
                        stock_quantity = item[3]
                        
                        
                        if quantity > stock_quantity:
                            print(f"Sorry, the quantity of book with ID {book_id} is insufficient.")
                            can_place_order = False
                            break

                        total_item_value = price * quantity
                        total_value += total_item_value
                    
                    if not can_place_order:
                        print("Your order cannot be placed due to insufficient quantity.")
                        continue

                    print("Total Cart Value:", total_value)

                    
                    address_choice = input("Do you want to use your saved address? (yes/no): ").lower()
                    if address_choice == "yes":
                       
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
                        
                        house_no = int(input("Enter your house number: "))
                        street_name = input("Enter your street name (press Enter to skip): ")
                        city = input("Enter your city: ")
                        state = input("Enter your state: ")
                        zip_code = int(input("Enter your zip code: "))

                      
                        cursor.execute("INSERT INTO Address (House_NO, Street_Name, City, State, Zip) VALUES (%s, %s, %s, %s, %s)",
                                        (house_no, street_name, city, state, zip_code))
                        mydb.commit()

                        
                        address_id = cursor.lastrowid

                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")

                    
                    payment_mode = input("Enter mode of payment (e.g., Credit Card, PayPal, etc.): ")

                   
                    cursor.execute("INSERT INTO customer_order (customer_id, total_price, address, payment_mode) VALUES (%s, %s, %s, %s)",
                                    (cust_id, total_value, address_id, payment_mode))
                    order_id = cursor.lastrowid

                   
                    for item in cart_items:
                        book_id = item[0]  
                        quantity = item[2] 

                        cursor.execute("UPDATE Book SET book_availability = book_availability - %s WHERE book_id = %s", (quantity, book_id))

                    
                    for item in cart_items:
                        book_id = item[0]  
                        quantity = item[2]

                        cursor.execute("INSERT INTO OrderItem (book_id, order_id, quantity) VALUES (%s, %s, %s)",
                                        (book_id, order_id, quantity))

                    # Clear the cart after placing the order
                    cursor.execute("DELETE FROM Cart WHERE customer_id = %s", (cust_id,))
                    mydb.commit()

                    print("Your order has been successfully placed. Thank you for shopping with us!")
                    # Display order summary
                    # cursor.execute("CALL GenerateOrderSummary(%s)", (order_id,))
                    # order_summary = cursor.fetchall()
                    # for summary in order_summary:
                    #     print(summary)

        elif choice == 10:
            
            try:
                cursor.execute("START TRANSACTION;")
                
                # Delete the cart for the given customer_id
                cursor.execute("DELETE FROM Cart WHERE customer_id = %s", (cust_id,))
                
               
                mydb.commit()

               
                cursor.execute("INSERT INTO Cart (customer_id) VALUES (%s)", (cust_id,))
                
                
                mydb.commit()

                print("Your cart has been cleared and a new cart has been created.")

            except mysql.connector.Error as e:
                print("Error:", str(e))
                mydb.rollback()  # Rollback the transaction in case of an error

        if choice == 11:
            
            book_id = int(input("Enter the Book ID: "))
            
           
            cursor.execute("SELECT b.*, bd.book_description FROM Book b LEFT JOIN BookDescription bd ON b.book_id = bd.book_id WHERE b.book_id = %s", (book_id,))
            book_details = cursor.fetchone()
            
            if book_details:
                print("Book Details:")
                print("Book ID:", book_details[0])
                print("Title:", book_details[1])
                print("Author:", book_details[2])
                print("Genre:", book_details[3])
                print("Series:", book_details[4])
                print("Publication:", book_details[5])
                print("Availability:", book_details[6])
                print("Vendor ID:", book_details[7])
                print("Price:", book_details[8])
                print("Description:", book_details[9])  
                print()
                
               
                cursor.execute("SELECT rating, content FROM ProductReview WHERE book_id = %s", (book_id,))
                reviews = cursor.fetchall()
                
                if reviews:
                    print("Reviews:")
                    for review in reviews:
                        print("Rating:", review[0])
                        print("Content:", review[1])
                        print()
                else:
                    print("No reviews found for this book.")
            else:
                print("Book not found.")
                
        if choice == 12:
            try:
                # Begin transaction
                cursor.execute("START TRANSACTION")
                
                # Fetch orders placed by the customer
                cursor.execute("SELECT order_id FROM customer_order WHERE customer_id = %s", (cust_id,))
                orders = cursor.fetchall()

                if orders:
                    print("Your Orders:")
                    for order in orders:
                        order_id = order[0]
                        
                        cursor.execute("SELECT b.book_id, b.book_title FROM OrderItem oi JOIN Book b ON oi.book_id = b.book_id WHERE oi.order_id = %s", (order_id,))
                        books_in_order = cursor.fetchall()
                        
                        if books_in_order:
                            print(f"Order ID: {order_id}")
                            print("Books Purchased:")
                            for book in books_in_order:
                                print(f"Book ID: {book[0]}, Title: {book[1]}")
                               
                                rating = int(input("Enter rating (0-5): "))
                                content = input("Enter review content: ")
                                
                             
                                cursor.execute("INSERT INTO ProductReview (book_id, customer_id, rating, content) VALUES (%s, %s, %s, %s)", (book[0], cust_id, rating, content))
                        
                else:
                    print("You haven't placed any orders yet.")
                
                # Commit transaction
                mydb.commit()
                print("Transaction successful!")
            
            except mysql.connector.Error as err:
                # Rollback transaction if any error occurs
                print("Error:", err)
                print("Rolling back changes...")
                mydb.rollback()

        elif choice == 13:
           
            print("Signing out...")
            break
            
        else:
           
            continue
    login()
    
def delete_book(vendor_id, book_id, quantity):
    try:
        lock.acquire()
        # Start a transaction
        cursor.execute("START TRANSACTION")

        # Check if the book belongs to the vendor and has enough quantity to delete
        cursor.execute("SELECT book_availability FROM Book WHERE book_id = %s AND VendorID = %s FOR UPDATE", (book_id, vendor_id))
        book = cursor.fetchone()
        if book:
            current_quantity = book[0]
            if current_quantity >= quantity:
                # Perform the deletion
                new_quantity = current_quantity - quantity
                cursor.execute("UPDATE Book SET book_availability = %s WHERE book_id = %s AND VendorID = %s", (new_quantity, book_id, vendor_id))
                print(f"{quantity} books deleted successfully.")
            else:
                print("Insufficient quantity to delete.")
        else:
            print("Invalid Book ID or book belongs to another vendor.")

        # Commit the transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback the transaction if an error occurs
        mydb.rollback()
        print("Error:", err)
    finally:
        # Release the lock
        lock.release()

        
def VendorCommands(vendor_number):
    while True:
        cursor.execute("SELECT VendorID FROM Vendor WHERE phone_number = %s", (vendor_number,))
        vendor_id = cursor.fetchone()[0]  
        
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
         
            search_filters = {}
            
          
            book_id = input("Enter Book ID (press Enter to skip): ")
            if book_id:
                search_filters['book_id'] = book_id
            
            title = input("Enter Title (press Enter to skip): ")
            if title:
                search_filters['book_title'] = title  
                
            author = input("Enter Author (press Enter to skip): ")
            if author:
                search_filters['book_author'] = author 
                
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
                
                search_filters['book_price'] = price   
                
            
            
            sql_query = "SELECT * FROM Book JOIN Vendor ON Book.VendorID = Vendor.VendorID WHERE Vendor.VendorID = %s", (VendorID,)
            conditions = []
            for key, value in search_filters.items():
                if key == 'book_price':
                    conditions.append(f"{key} < {value}")
                else:
                    
                    conditions.append(f"{key} = '{value}'")
            
           
            sql_query += " OR ".join(conditions)
            print(sql_query)
           
            cursor.execute(sql_query)
            search_results = cursor.fetchall()

            
           
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
            book_id_to_delete = int(input("Enter the ID of the book you want to delete: "))
            quantity_to_delete = int(input("Enter the quantity to delete: "))
            delete_book(vendor_id, book_id_to_delete, quantity_to_delete)
            
        elif choice == '5':
           
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
            continue
    
    login()
    1

 
def DeliveryAgentCommands():
    while True:
        try:
            agent_id = int(input("Enter Delivery Agent ID: "))
            cursor.execute("SELECT * FROM DeliveryAgent WHERE daID = %s", (agent_id,))
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
                    print("Availability:", agent_info[3])
                    print("Phone Number:", agent_info[4])

                else:
                    print("Vendor not found.")
            
            elif choice == '2':
                availability = input("Enter your availability (e.g., 'Available' or 'Unavailable'): ")
                cursor.execute("UPDATE DeliveryAgent SET availability = %s WHERE daID = %s", (availability, agent_id))
                mydb.commit() 
                print("Availability updated successfully.")

            elif choice == '3':
                area_servicing = input("Enter the area you are servicing: ")
                
                cursor.execute("ALTER TABLE DeliveryAgent ADD IF NOT EXISTS area_servicing VARCHAR(255)")
                
                cursor.execute("UPDATE DeliveryAgent SET area_servicing = %s WHERE daID = %s", (area_servicing, agent_id))
                mydb.commit()
                
                print("Area servicing updated successfully.")

            elif choice == '4':
                cursor.execute("SELECT * FROM Orders WHERE daID = %s AND delivery_status = 'In transit'", (agent_id,))
                current_orders = cursor.fetchone()
                print("Order ID",current_orders[0])
                print("Order Status",current_orders[1])
                print("Order Date",current_orders[2])
                print("Customer ID",current_orders[4])

            elif choice == '5':
                cursor.execute("SELECT * FROM Orders WHERE daID = %s AND (delivery_status = 'Delivered' OR delivery_status = 'Cancelled')", (agent_id,))
                past_orders= cursor.fetchone()
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

# def print_all_vendors():
#     # Execute SQL query to fetch all vendors
#     cursor.execute("SELECT * FROM Vendor")
#     vendors = cursor.fetchall()
    
#     # Print all vendors
#     for vendor in vendors:
#         print(vendor)
# print_all_vendors()

# Function to process Warehouse

def add_warehouse():
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")

        owner_name = input("Enter owner's name: ")
        street = input("Enter street address: ")
        city_area = input("Enter city/area: ")
        province_state = input("Enter province/state: ")
        country = input("Enter country: ")
        pincode = int(input("Enter pincode: "))

        full_address = f"{owner_name}, {street}, {city_area}, {province_state}, {country}, {pincode}"

        cursor.execute("INSERT INTO Warehouse (address, pincode) VALUES (%s, %s)", (full_address, pincode))
        
        # Commit transaction
        mydb.commit()
        print("Warehouse added successfully.")
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()

def remove_warehouse_by_id(warehouse_id):
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        cursor.execute("DELETE FROM Warehouse WHERE warehouseID = %s", (warehouse_id,))
       
        mydb.commit()
        print("Warehouse removed successfully.")
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()
        
def update_warehouse(warehouse_id):
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        print("Select attribute to update:")
        print("1. Address")
        print("2. Pincode")
        option = int(input("Enter the option: "))

        if option == 1:
            new_address = input("Enter new address: ")
            cursor.execute("UPDATE Warehouse SET address = %s WHERE warehouseID = %s", (new_address, warehouse_id))
        elif option == 2:
            new_pincode = int(input("Enter new pincode: "))
            # Fetch current address of the warehouse
            cursor.execute("SELECT address FROM Warehouse WHERE warehouseID = %s", (warehouse_id,))
            current_address = cursor.fetchone()[0]
            # Replace the current pincode with the new pincode in the address
            updated_address = current_address.replace(str(warehouse_id), str(new_pincode))
            cursor.execute("UPDATE Warehouse SET pincode = %s, address = %s WHERE warehouseID = %s", (new_pincode, updated_address, warehouse_id))
        else:
            print("Invalid option.")
            return

        # Commit transaction
        mydb.commit()
        print("Warehouse updated successfully.")
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()
        
        
def show_all_warehouses():
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        cursor.execute("SELECT * FROM Warehouse")
        warehouses = cursor.fetchall()
        time.sleep(90)
        if warehouses:
            print("All Warehouses:")
            for warehouse in warehouses:
                print("Warehouse ID:", warehouse[0])
                print("Address:", warehouse[1])
                print("Pincode:", warehouse[2])
                print()  # Empty line for separation
        else:
            print("No warehouses found.")
            
        # Commit transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()





# Function to display all pending vendor requests
def display_pending_vendors():
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        cursor.execute("SELECT VendorID, vendor_name, Email FROM PendingVendorRequests WHERE approved = False")
        pending_vendors = cursor.fetchall()
        if pending_vendors:
            print("Pending Vendor Requests:")
            for vendor in pending_vendors:
                print(f"ID: {vendor[0]}, Name: {vendor[1]}, Email: {vendor[2]}")
        else:
            print("No pending vendor requests.")
            
        # Commit transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()
        


def approve_vendor(vendor_id):
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        cursor.execute("SELECT * FROM PendingVendorRequests WHERE VendorID = %s", (vendor_id,))
        vendor_info = cursor.fetchone()
        if vendor_info:
            
            cursor.execute("INSERT INTO Vendor (vendor_name, Email, Age, Phone_number, vendor_password) VALUES (%s, %s, %s, %s, %s)",
                           (vendor_info[1], vendor_info[2], vendor_info[3], vendor_info[4], vendor_info[5]))
            print("Vendor approved and added to Vendor list.")
            
            cursor.execute("UPDATE PendingVendorRequests SET Message = 'Your request is approved and you are now a Vendor', approved = True WHERE VendorID = %s", (vendor_id,))

           
            cursor.execute("""CREATE EVENT IF NOT EXISTS DeleteApprovedVendorEvent
                                ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 2 MINUTE
                                DO
                                    DELETE FROM PendingVendorRequests WHERE VendorID = %s""", (vendor_id,))
            print("Event created to delete approved vendor from pending list after 2 minutes.")

         
            cursor.execute("SELECT * FROM Vendor ORDER BY VendorID DESC LIMIT 3")
            vendor_list = cursor.fetchall()
            print("Last 3 entries in the Vendor table:")
            for vendor in vendor_list:
                print(vendor)
                
        else:
            print("Invalid vendor ID.")
        
        # Commit transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()


def disapprove_vendor(vendor_id):
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
      
        cursor.execute("SELECT VendorID FROM PendingVendorRequests WHERE VendorID = %s", (vendor_id,))
        result = cursor.fetchone()
        if result:

            cursor.execute("UPDATE PendingVendorRequests SET Message = %s WHERE VendorID = %s", ("Your request has been disapproved by the vendor", vendor_id))
            print("Vendor request disapproved. Message updated.")
        else:
            print("Vendor ID not found in the list of pending vendor requests.")
        
        # Commit transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()

def ban_vendor(vendor_id):
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        cursor.execute("UPDATE Vendor SET vendor_banned = True WHERE VendorID = %s", (vendor_id,))
        print("Vendor banned successfully.")
        
        # Commit transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()

def ban_customer(customer_id):
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        cursor.execute("UPDATE Customer SET is_banned = True WHERE customer_id = %s", (customer_id,))
        print("Customer banned successfully.")
        
        # Commit transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...") 
        mydb.rollback()

def unban_vendor(vendor_id):
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        cursor.execute("UPDATE Vendor SET vendor_banned = False WHERE VendorID = %s", (vendor_id,))
        print("Vendor unbanned successfully.")
        
        # Commit transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()

def unban_customer(customer_id):
    try:
        # Begin transaction
        cursor.execute("START TRANSACTION")
        
        cursor.execute("UPDATE Customer SET is_banned = False WHERE customer_id = %s", (customer_id,))
        print("Customer unbanned successfully.")
        
        # Commit transaction
        mydb.commit()
    except mysql.connector.Error as err:
        # Rollback transaction if any error occurs
        print("Error:", err)
        print("Rolling back changes...")
        mydb.rollback()


def update_availability(agent_id, new_availability):
    # cursor = mydb.cursor()
    try:
        # Acquire lock before accessing shared resource
        lock.acquire()
        
        cursor.execute("START TRANSACTION;")
        cursor.execute(
            "UPDATE DeliveryAgent SET availability = %s WHERE daID = %s",
            (new_availability, agent_id,)
        )
        print(f"Setting availability to {new_availability} for agent {agent_id}")
       
        import time; time.sleep(1)
        mydb.commit()
        print(f"Availability updated to {new_availability} for agent {agent_id}")
    except mysql.connector.Error as e:
        print("Error:", str(e))
        mydb.rollback()
    finally:
       
        lock.release()
        # cursor.close()

def change_cust_password(cust_phone_number, new_password):
    
    try:
        # Acquire lock before accessing shared resource
        lock.acquire()
        
        cursor.execute("START TRANSACTION;")
        print(f"Attempting to update password for customer with phone number: {cust_phone_number}")
        cursor.execute(
            "UPDATE Customer SET customer_password = %s WHERE phone_number = %s",
            (new_password, cust_phone_number,)
        )
        
        import time; time.sleep(2)
        mydb.commit()
        print(f"Password for customer {cust_phone_number} updated to {new_password}")
    except mysql.connector.Error as e:
        print("Error:", str(e))
        mydb.rollback()
    finally:
        # Release the lock after using shared resource
        lock.release()
        # cursor.close()


def AdminCommands():
    while True: 
        print("Admin Commands:")
        print("1. Manage Pending Vendor requests.")
        print("2. Warehouse Management.")
        print("3. Ban a Vendor / Ban a Customer.")
        print("4. UnBan a Customer/Vendor.")
        option = int(input("Enter the Option:"))
        
        if option == 1:
            while True:  
                print("1. Show All Pending Vendor requests.")
                print("2. Approve/Disapprove Vendor.")
                sub_option = int(input("Enter the Option:"))
                if sub_option == 1:
                    display_pending_vendors()
                elif sub_option == 2:
                    print("1. Approve the Vendor.")
                    print("2. Disapprove the Vendor.")
                    sub_option2 = int(input("Enter the Option:"))
                    if sub_option2 == 1:
                        vendor_id = int(input("Enter the ID of the vendor you want to approve: "))
                        approve_vendor(vendor_id)
                    elif sub_option2 == 2:
                        vendor_id = int(input("Enter the ID of the vendor you want to disapprove: "))
                        disapprove_vendor(vendor_id)
                    else:
                        print("Please select a valid sub-option.")
                else:
                    print("Please select a valid option.")
                if input("Do you want to continue with Vendor Management? (yes/no): ").lower() != 'yes':
                    break

        elif option == 2:
            while True:  
                print("1. Add Warehouse")
                print("2. Remove Warehouse")
                print("3. Update Warehouse")
                print("4. Show All the Warehouses.")
                sub_option = int(input("Enter the option:"))
                if sub_option == 1:
                    add_warehouse()
                elif sub_option == 2:
                    wid = int(input("Enter the warehouse id to remove:"))
                    remove_warehouse_by_id(wid)
                elif sub_option == 3:
                    wid = int(input("Enter the warehouse id to update:"))
                    update_warehouse(wid)
                elif sub_option == 4:
                    show_all_warehouses()
                else:
                    print("Please select a valid option.")
                if input("Do you want to continue with Warehouse Management? (yes/no): ").lower() != 'yes':
                    break

        elif option == 3:
            while True:  
                print("1. Ban Vendor")
                print("2. Ban Customer")
                sub_option = int(input("Enter 1 to ban Vendor or 2 to ban Customer:"))
                if sub_option == 1:
                    vendor_id = int(input("Enter the ID of the vendor you want to ban: "))
                    ban_vendor(vendor_id)
                elif sub_option == 2:
                    customer_id = int(input("Enter the ID of the customer you want to ban: "))
                    ban_customer(customer_id)
                else:
                    print("Please select a valid option.")
                if input("Do you want to continue with Ban Management? (yes/no): ").lower() != 'yes':
                    break
                
        elif option == 4:
            while True:  
                print("1. Unban Vendor")
                print("2. Unban Customer")
                sub_option = int(input("Enter 1 to unban Vendor or 2 to unban Customer:"))
                if sub_option == 1:
                    vendor_id = int(input("Enter the ID of the vendor you want to unban: "))
                    unban_vendor(vendor_id)
                elif sub_option == 2:
                    customer_id = int(input("Enter the ID of the customer you want to unban: "))
                    unban_customer(customer_id)
                else:
                    print("Please select a valid option.")
                if input("Do you want to continue with Unban Management? (yes/no): ").lower() != 'yes':
                    break
                    
        else:
            print("Invalid option.")
            
        if input("Do you want to continue? (yes/no): ").lower() == 'no':
            break



def homepage():
    while True:
        print("Welcome to the Home Page!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        
        choice = input("Please select an option: ")

        if choice == "1":
            # Call the sign_up function
            signup()
        elif choice == "2":
            # Call the log_in function
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Please select a valid option.")


@app.route('/Signup', methods=['POST'])
def Signup():
    data = request.get_json()
    # Extract data and perform SQL INSERT operation
    # ...
    return jsonify({"message": "Sign up successful"})

if __name__ == '__main__':
    app.run(debug=True)
# def conflict_3():
    
#     vendor_id = 1  # Replace 1 with the actual vendor ID
#     book_id = 1    # Replace 1 with the actual book ID
#     quantity = 10  # Specify the quantity to delete
#     # Create two threads for concurrent deletion
#     thread1 = threading.Thread(target=delete_book, args=(vendor_id, book_id, quantity))
#     thread2 = threading.Thread(target=delete_book, args=(vendor_id, book_id, quantity))

#     # Start both threads
#     thread1.start()
#     thread2.start()

#     # Wait for both threads to finish
#     thread1.join()
#     thread2.join()

#     # Close the database connection
#     cursor.close()
#     mydb.close()


# def conflict_1():
#     agent_id = 1  

#     # Create two threads for concurrent setting availablity 
#     thread1 = threading.Thread(target=update_availability, args=(agent_id, "Available"))
#     thread2 = threading.Thread(target=update_availability, args=(agent_id, "Unavailable"))
    
    
#     thread1.start()
#     thread2.start()

#      # Wait for both threads to finish
#     thread1.join()
#     thread2.join()
    
#     # Close the database connection
#     cursor.close()
#     mydb.close()
    


# def conflict_2():
#     cust_phone_number = '8619631019' 

#     thread1 = threading.Thread(target=change_cust_password, args=(cust_phone_number, "Password123"))
#     thread2 = threading.Thread(target=change_cust_password, args=(cust_phone_number, "Secure456"))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()
#     cursor.close()
#     mydb.close()
    


# lock = threading.Lock()

# # conflict_1()

# # conflict_2()

# # conflict_3()
# # homepage()


# def vendor_signup4(cursor, mydb):
#     print("Vendor Signup")
#     name = input("Enter vendor name: ")
#     email = input("Enter email: ")
#     vend_password = input("Enter your password: ")
    
#     while True:
#         try:
#             age = int(input("Enter age: "))
#             break
#         except ValueError:
#             print("Please enter a valid age (numeric value).")

#     phone_number = input("Enter phone number: ")
    
#     while True:
#         try:
#             phone_number = int(phone_number)
#             break
#         except ValueError:
#             print("Please enter a valid phone number (numeric value).")
#             phone_number = input("Enter phone number: ")
    
#     try:
#         # Start first transaction
#         cursor.execute("START TRANSACTION")
        
#         cursor.execute("INSERT INTO Vendor (vendor_name, Email, Age, Phone_number, vendor_password) VALUES (%s, %s, %s, %s, %s)",
#                        (name, email, age, phone_number, vend_password))
        
#         mydb.commit()
        
        
#         print("First Vendor signup successful!")
#         mydb.rollback()
#     except mysql.connector.Error as err:
#         print("Error:", err)
#         print("Rolling back first transaction...")
#         mydb.rollback()

#     try:
#         # Start second transaction
#         cursor.execute("START TRANSACTION")
        
#         # Perform some other operation (for demonstration purposes, you can just print something)
#         print("Second transaction started.")
#         cursor.execute("INSERT INTO Vendor (vendor_name, Email, Age, Phone_number, vendor_password) VALUES (%s, %s, %s, %s, %s)",
#                        (name, "niket1234@gmgm.com", age, 9999999999, vend_password))
        
#         mydb.rollback()
        
  
#     except mysql.connector.Error as err:
#         print("Error:", err)
        

# vendor_signup4(cursor, mydb)















