# 📚 DBMS Bookstore Application

A comprehensive database-driven bookstore management system built with Python and SQL, featuring role-based access control and complete e-commerce functionality.

## 🌟 Project Overview

This bookstore application is a full-featured database management system that handles multiple user roles, inventory management, order processing, and delivery tracking. The system demonstrates advanced database design principles and implements a complete business workflow.

## 🏗️ Architecture & Technologies

- **Backend**: Python with SQL integration
- **Database**: SQL Server with normalized schema
- **Interface**: Command Line Interface (CLI)
- **Authentication**: Role-based access control system
- **Design Pattern**: Multi-tier architecture with separation of concerns

## 🚀 Features Implemented

### 👥 Multi-Role User Management
- **Customer Management**: Registration, authentication, profile management
- **Vendor Management**: Business registration, inventory control, approval workflow
- **Delivery Agent Management**: Area coverage, availability tracking, order assignments
- **Admin Management**: System oversight, user management, warehouse operations

### 🛒 E-Commerce Functionality
- **Product Catalog**: Comprehensive book inventory with search capabilities
- **Shopping Cart**: Add, remove, and manage items before purchase
- **Order Processing**: Complete order lifecycle from cart to delivery
- **Payment Integration**: Order placement and transaction handling

### 📦 Inventory & Warehouse Management
- **Stock Control**: Real-time inventory tracking and updates
- **Warehouse Operations**: Multi-location inventory management
- **Vendor Integration**: Direct vendor inventory management
- **Automated Notifications**: Low stock alerts and availability updates

### 🚚 Delivery System
- **Agent Assignment**: Automatic delivery agent matching based on area
- **Order Tracking**: Real-time order status updates
- **Delivery History**: Complete delivery records and performance tracking
- **Area Management**: Service area coverage and optimization

### 📊 Review & Rating System
- **Book Reviews**: Customer feedback and rating system
- **Delivery Agent Reviews**: Service quality assessment
- **Review Management**: Display and management of all reviews

### 🔐 Advanced Security Features
- **Role-Based Access Control**: Distinct permissions for each user type
- **User Authentication**: Secure login and session management
- **Admin Controls**: Ban/unban functionality for users
- **Data Validation**: Input sanitization and validation

## 📋 Installation & Setup

### Prerequisites
- Python 3.x installed
- SQL Server or compatible database system
- Required Python packages for database connectivity

### Installation Steps

1. **Database Setup**
   ```bash
   # Run the database schema creation
   Run table.sql in your SQL Server
   
   # Populate initial data
   Run Entry_Bookstore.sql in your SQL Server
   ```

2. **Application Configuration**
   ```bash
   # Configure database connection in sql.py
   # Update connection parameters at the beginning of the script
   # Set server, database, username, and password
   ```

3. **Run Application**
   ```bash
   python sql.py
   ```

## 🎯 User Workflows

### Customer Journey
1. **Registration/Login** → Account creation or authentication
2. **Browse Catalog** → Search and view available books
3. **Shopping** → Add books to cart, manage quantities
4. **Order Placement** → Review cart and place orders
5. **Order Tracking** → Monitor delivery status
6. **Review System** → Rate books and delivery experience

### Vendor Operations
1. **Business Registration** → Apply for vendor status
2. **Inventory Management** → Add, edit, delete books
3. **Stock Control** → Update quantities and availability
4. **Sales Monitoring** → Track orders and performance
5. **Profile Management** → Update business information

### Delivery Agent Workflow
1. **Registration** → Join as delivery agent
2. **Area Setup** → Configure service areas
3. **Availability Management** → Set working status
4. **Order Handling** → Process assigned deliveries
5. **Performance Tracking** → Monitor delivery history

### Admin Dashboard
1. **Vendor Approval** → Review and approve vendor applications
2. **User Management** → Ban/unban users as needed
3. **Warehouse Operations** → Manage storage locations
4. **System Oversight** → Monitor overall system health

## 🗄️ Database Schema Highlights

### Core Entities
- **Users**: Comprehensive user management with role differentiation
- **Books**: Detailed book catalog with metadata
- **Orders**: Complete order lifecycle tracking
- **Inventory**: Real-time stock management
- **Warehouses**: Multi-location storage system
- **Reviews**: Customer feedback and rating system

### Key Relationships
- User-Role associations with proper constraints
- Vendor-Book relationships for inventory management
- Order-Delivery agent assignments
- Warehouse-Book location tracking

## 🔧 Technical Implementation

### Database Features
- **Normalized Schema**: Efficient data organization with minimal redundancy
- **Referential Integrity**: Proper foreign key relationships
- **Indexing**: Optimized query performance
- **Stored Procedures**: Complex business logic implementation
- **Triggers**: Automated data consistency maintenance

### Application Features
- **Error Handling**: Comprehensive exception management
- **Input Validation**: Data integrity and security measures
- **Session Management**: User state maintenance
- **Logging**: Activity tracking and debugging support

## 📈 Performance & Scalability

- **Optimized Queries**: Efficient database operations
- **Connection Pooling**: Resource management
- **Caching Strategy**: Improved response times
- **Modular Design**: Easy feature additions and modifications

## 🛡️ Security Measures

- **SQL Injection Prevention**: Parameterized queries
- **Authentication System**: Secure user verification
- **Role-Based Permissions**: Granular access control
- **Data Encryption**: Sensitive information protection

## 🚀 Future Enhancements

- Web-based interface development
- Mobile application integration
- Advanced analytics and reporting
- Payment gateway integration
- Real-time notifications system
- Machine learning recommendations

## 👨‍💻 Development Achievements

This project demonstrates proficiency in:
- **Database Design & Management**: Complex schema design with proper normalization
- **Python Programming**: Object-oriented design and database integration
- **System Architecture**: Multi-tier application development
- **Business Logic Implementation**: Complete e-commerce workflow
- **User Experience Design**: Intuitive CLI interface
- **Security Implementation**: Comprehensive access control system

## 📞 Support & Documentation

For detailed command references and troubleshooting, refer to the user guide documentation included in the project.

---

**Project Status**: ✅ Fully Functional  
**Last Updated**: 2024  
**Version**: 1.0  

*This project showcases a complete database-driven application with real-world business