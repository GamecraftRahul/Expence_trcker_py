-- Create the database
CREATE DATABASE IF NOT EXISTS expense_manager_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Use the new database
USE expense_manager_db;

-- Create the expenses table
CREATE TABLE IF NOT EXISTS expenses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date DATE NOT NULL,
  category VARCHAR(100) NOT NULL,
  description VARCHAR(255),
  amount DECIMAL(10,2) NOT NULL,
  payment_method VARCHAR(50),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Insert some sample data
INSERT INTO expenses (date, category, description, amount, payment_method) VALUES
('2025-10-01', 'Food', 'Breakfast at cafe', 4.50, 'Card'),
('2025-10-02', 'Transport', 'Taxi to office', 8.00, 'Cash'),
('2025-10-03', 'Groceries', 'Weekly shopping', 35.20, 'Card'),
('2025-10-05', 'Entertainment', 'Cinema', 12.00, 'Card'),
('2025-09-30', 'Bills', 'Electricity bill', 48.75, 'Online');
