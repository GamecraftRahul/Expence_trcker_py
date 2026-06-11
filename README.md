# Expense Management System

A desktop-based Expense Management System developed using **Python**, **Tkinter**, **ttkbootstrap**, **MySQL**, and **Pandas**. The application helps users manage daily expenses, categorize spending, generate summaries, and export records to CSV files through an intuitive graphical interface.

---

## Features

- Add new expense records
- Delete selected expenses
- View all expenses in a table format
- Category-wise expense summary
- Export expense data to CSV
- Insert sample data for testing
- Modern GUI using ttkbootstrap
- MySQL database integration
- Automatic data refresh
- Expense tracking by date and payment method

---

## Technologies Used

- Python 3.x
- Tkinter
- ttkbootstrap
- MySQL
- mysql-connector-python
- Pandas

---

## Project Structure

```text
Expense Management System/
│
├── expense_tracking_sys.py
├── expense_management.sql
├── README.md
```

---

## Database Setup

### Step 1: Create Database

```sql
CREATE DATABASE expense_manager_db;
USE expense_manager_db;
```

### Step 2: Create Expenses Table

```sql
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    category VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system
```

### Install Required Libraries

```bash
pip install ttkbootstrap
pip install mysql-connector-python
pip install pandas
```

---

## Configure Database Connection

Open the Python file and update the MySQL credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_PASSWORD',
    'database': 'expense_manager_db'
}
```

---

## Running the Application

```bash
python expense_tracking_sys.py
```

---

## Application Modules

### Add Expense

- Select expense date
- Enter category
- Enter description
- Enter amount
- Enter payment method
- Save expense record

### Delete Expense

- Select one or multiple records
- Delete selected expenses

### Expense Summary

Displays category-wise total spending:

```text
Food: ₹500.00
Transport: ₹250.00
Bills: ₹1200.00
```

### Export CSV

- Export all expense records
- Save data as a CSV file
- Useful for reports and backups

### Sample Data

Automatically inserts sample expense records for testing and demonstration.

---

## User Interface Components

- Main Dashboard
- Expense Table
- Add Expense Window
- Summary Dialog
- Export File Dialog
- Message Boxes

---

## Database Operations

### Create

Add new expense records.

### Read

Display all stored expenses in a Treeview table.

### Delete

Remove selected records from the database.

### Aggregate

Generate category-wise expense summaries using SQL aggregation.

---

## Validation Features

- Required field validation
- Numeric amount validation
- Database connection error handling
- Record selection validation before deletion

---

## CSV Export Feature

The system allows users to export all expense records:

```csv
id,date,category,description,amount,payment_method
1,2025-10-01,Food,Lunch,120.00,Cash
2,2025-10-02,Transport,Metro,45.50,Card
```

---

## Screenshots

Add screenshots of:

- Main Dashboard
- Expense List
- Add Expense Form
- Expense Summary
- CSV Export Feature

---

## Future Enhancements

- Expense Editing Feature
- Monthly Expense Reports
- Income Management
- Budget Tracking
- Expense Charts and Graphs
- PDF Report Generation
- Search and Filter System
- User Authentication
- Cloud Database Support
- Multi-User Access

---

## Learning Outcomes

This project demonstrates:

- Python GUI Development
- MySQL Database Integration
- CRUD Operations
- Data Validation
- CSV Export Functionality
- SQL Aggregation Queries
- Desktop Application Development
- Expense Tracking System Design

---

## Author

**Rahul Kulkarni**

Python Developer | MySQL Developer

---

## License

This project is developed for educational and learning purposes only.

---

## Project Overview

The Expense Management System is designed to help users track and organize their daily expenses efficiently. It provides features for recording expenses, viewing spending history, generating category-wise summaries, and exporting records for analysis. This project is ideal for learning database-driven desktop application development using Python and MySQL.
