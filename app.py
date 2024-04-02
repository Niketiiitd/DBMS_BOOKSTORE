from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuration for the SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bookstore.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model definition for Address
class Address(db.Model):
    Address_ID = db.Column(db.Integer, primary_key=True)
    House_NO = db.Column(db.Integer, nullable=False)
    Street_Name = db.Column(db.String(255))
    City = db.Column(db.String(255), nullable=False)
    State = db.Column(db.String(255), nullable=False)
    Zip = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Address {self.Address_ID}>'

# Model definition for Book
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(255), nullable=False)
    book_author = db.Column(db.String(255), nullable=False)
    book_genre = db.Column(db.String(255), nullable=False)
    book_series = db.Column(db.String(255), nullable=False)
    book_publication = db.Column(db.String(255), nullable=False)
    book_availability = db.Column(db.Integer, nullable=False)
    VendorID = db.Column(db.Integer, db.ForeignKey('vendor.VendorID'))
    book_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.book_title}>'

# Model definition for Customer
class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255))
    Address_ID = db.Column(db.Integer, db.ForeignKey('address.Address_ID'), nullable=False)
    phone_number = db.Column(db.BigInteger, unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    customer_password = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Customer {self.customer_name}>'

# Model definition for DeliveryAgent
class DeliveryAgent(db.Model):
    daID = db.Column(db.Integer, primary_key=True)
    da_name = db.Column(db.String(255), nullable=False)
    da_password = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.String(20), nullable=False)
    da_phone_no = db.Column(db.BigInteger, unique=True, nullable=False)

    def __repr__(self):
        return f'<DeliveryAgent {self.da_name}>'

# Model definition for Warehouse
class Warehouse(db.Model):
    warehouseID = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), unique=True, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Warehouse {self.address}>'

# Model definition for Orders
class Orders(db.Model):
    orderID = db.Column(db.Integer, primary_key=True)
    Order_status = db.Column(db.String(255), nullable=False)
    orderDATE = db.Column(db.Date, nullable=False)
    totalPrice = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))

    def __repr__(self):
        return f'<Orders {self.orderID}>'

# Model definition for ProductReview
class ProductReview(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<ProductReview {self.review_id}>'

# Model definition for DAgentReview
class DAgentReview(db.Model):
    da_review_id = db.Column(db.Integer, primary_key=True)
    daID = db.Column(db.Integer, db.ForeignKey('delivery_agent.daID'), nullable=False)
    agent_review = db.Column(db.Integer, nullable=False)
    agent_review_description = db.Column(db.String(512))
    agent_review_date = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<DAgentReview {self.da_review_id}>'

# Model definition for BookDescription
class BookDescription(db.Model):
    book_description_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    book_description = db.Column(db.String(512))

    def __repr__(self):
        return f'<BookDescription {self.book_description_id}>'

# Model definition for OrderItem
class OrderItem(db.Model):
    orderItem_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    orderID = db.Column(db.Integer, db.ForeignKey('orders.orderID'), nullable=False)
    quantity = db.Column(db.BigInteger)

    def __repr__(self):
        return f'<OrderItem {self.orderItem_id}>'

# Model definition for ISBNInfo
class ISBNInfo(db.Model):
    isbn_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    edition = db.Column(db.Integer)
    date_added = db.Column(db.String(50))
    date_written = db.Column(db.String(50))

    def __repr__(self):
        return f'<ISBNInfo {self.isbn_id}>'

# Model definition for StockQuantity
class StockQuantity(db.Model):
    stock_quantity_id = db.Column(db.Integer, primary_key=True)
    isbn_id = db.Column(db.Integer, db.ForeignKey('isbn_info.isbn_id'), nullable=False)
    number_of_books = db.Column(db.Integer, nullable=False)
    book_type = db.Column(db.String(50))

    def __repr__(self):
        return f'<StockQuantity {self.stock_quantity_id}>'

# Custom Flask command to create the database
@app.cli.command('create-db')
def create_db():
    """Creates the database."""
    db.create_all()
    print('Database created.')

# Route for vendor registration form submission
@app.route('/Registration/Vendor', methods=['POST'])
def register_vendor():
    # Get form data from request and insert into database
    # (Implementation goes here)
    pass

# Add routes for other functionalities as needed

if __name__ == '__main__':
    app.run(debug=True)
