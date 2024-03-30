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
                    CustomerCommands()
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

def CustomerCommands():
    print("1. View Books")
    print("2. Search")
    print("4. Show Cart")
    print("5. ")
    print("Hello")
    
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