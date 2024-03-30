import mysql.connector

mydb = mysql.connector.connect(
    host="Nikets-MacBook-Air.local",
    user="root",
    password="Niket@mac",
    database="bookshop",  # Specify the database
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

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
            # Customer login
            cust_number = input("Enter Customer Phone number: ")
            
            # Check phone number length
            if len(cust_number) != 10:
                print("Incorrect length of phone number. Please enter a 10-digit phone number.")
                continue
            
            cust_pass = input("Enter Customer Password: ")
            
            # Execute SQL query to check if customer exists
            cursor.execute("SELECT customer_password FROM Customer WHERE phone_number = %s", (cust_number,))
            result = cursor.fetchone()
            
            if result:
                db_cust_pass = result[0]  # Fetch the password from the database
                if db_cust_pass == cust_pass:
                    print("Customer Login Successful!")
                    CustomerCommands(cust_number)
                else:
                    print("Wrong Password!")
            else:
                print("No such customer found!")
        
        elif choice == 2:
            # Vendor login
            vendor_email = input("Enter Vendor Email: ")
            vendor_phone_number = input("Enter Vendor Phone number: ")
            vendor_pass = input("Enter Vendor Password: ")
            
            # Execute SQL query to check if vendor exists
            cursor.execute("SELECT vendor_name FROM Vendor WHERE Email = %s AND Phone_number = %s", (vendor_email, vendor_phone_number))
            result = cursor.fetchone()
            
            if result:
                print("Vendor Login Successful!")
                VendorCommands()
                # Additional logic for vendor login can be added here
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

def CustomerCommands(customer_number):
    
    while (True):
        cursor.execute("SELECT customer_id FROM Customer WHERE phone_number = %s", (customer_number,))
        result1 = cursor.fetchone()
        cust_id = result1[0]
        print("1. View Books")
        print("2. Search")
        print("3. Give order")
        print("4. Show order history")
        print("5. Show Cart")
        print("6. Show your personal details")
        print("7. Show book reviews given by you")
        print("8. Show DA_Agent reviews given by you")
        print("9. Logout")
        
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

        elif choice == 4:
            # Order history logic
            pass
        elif choice == 5:
            # Cart logic
            pass
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
            # DA_Agent reviews logic
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
          
        elif choice == 9:
            # Logout logic
            print("Signing out...")
            break
            
        else:
            print("Invalid choice. Please enter a valid option.")
    login()
    
def VendorCommands():
    print("Hello")
    
def DeliveryAgentCommands():
    print("hello")
    
def AdminCommands():
    print("hello")

login()

# def print_all_vendors():
#     # Execute SQL query to fetch all vendors
#     cursor.execute("SELECT * FROM Vendor")
#     vendors = cursor.fetchall()
    
#     # Print all vendors
#     for vendor in vendors:
#         print(vendor)
# print_all_vendors()