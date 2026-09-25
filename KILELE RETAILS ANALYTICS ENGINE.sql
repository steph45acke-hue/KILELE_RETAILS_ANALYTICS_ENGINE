-- 1. Create and select database
CREATE DATABASE IF NOT EXISTS kilele_retail_db;
USE kilele_retail_db;


DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS branches;

-- 2. Branches Table (Nairobi Sub-Counties)
CREATE TABLE branches (
    branch_id VARCHAR(20) PRIMARY KEY,
    branch_name VARCHAR(50) NOT NULL,
    sub_county VARCHAR(50) NOT NULL
);

-- 3. Categories Table 
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    parent_category_id INT NULL,
    CONSTRAINT fk_parent_category 
        FOREIGN KEY (parent_category_id) 
        REFERENCES categories(category_id) 
        ON DELETE CASCADE
);

-- 4. Products Table 
CREATE TABLE products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_product_category 
        FOREIGN KEY (category_id) 
        REFERENCES categories(category_id)
);

-- 5. Transactions Table 
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_id VARCHAR(20) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    quantity_sold INT NOT NULL,
    total_amount DECIMAL(12,2) NOT NULL,
    transaction_date DATE NOT NULL,
    CONSTRAINT fk_tx_branch FOREIGN KEY (branch_id) REFERENCES branches(branch_id),
    CONSTRAINT fk_tx_product FOREIGN KEY (product_id) REFERENCES products(product_id)
);



-- Insert Branches
INSERT INTO branches (branch_id, branch_name, sub_county) VALUES 
('CBD_01', 'Kilele CBD', 'Starehe'), 
('WST_02', 'Kilele Westlands', 'Westlands'),
('KSR_03', 'Kilele Kasarani', 'Kasarani'),
('LNG_04', 'Kilele Langata', 'Langata');

-- Insert Categories (Parent categories have NULL parent_id)
INSERT INTO categories (category_id, category_name, parent_category_id) VALUES 
(1, 'Food & Staples', NULL),
(2, 'Beverages & Dairy', NULL),
(3, 'Cereals & Flour', 1),
(4, 'Cooking Oils & Fats', 1),
(5, 'Tea & Hot Drinks', 2),
(6, 'Fresh Dairy', 2);

-- Insert Products
INSERT INTO products (product_id, product_name, category_id, unit_price) VALUES 
('PROD_01', 'Jogoo Unga 2kg', 3, 150.00),
('PROD_02', 'Supa Dafra Rice 5kg', 3, 650.00),
('PROD_03', 'Baraka Cooking Oil 3L', 4, 900.00),
('PROD_04', 'Kabras Sugar 2kg', 3, 280.00),
('PROD_05', 'Kericho Gold Tea 500g', 5, 250.00),
('PROD_06', 'Brookside Fresh Milk 500ml', 6, 65.00);

-- Insert Transactions 
INSERT INTO transactions (branch_id, product_id, quantity_sold, total_amount, transaction_date) VALUES 
-- CBD Branch Sales
('CBD_01', 'PROD_01', 15, 2250.00, '2026-08-28'),
('CBD_01', 'PROD_03', 6, 5400.00, '2026-08-29'),
('CBD_01', 'PROD_04', 20, 5600.00, '2026-08-30'),
('CBD_01', 'PROD_06', 30, 1950.00, '2026-09-01'),
('CBD_01', 'PROD_01', 12, 1800.00, '2026-09-02'),
('CBD_01', 'PROD_02', 10, 6500.00, '2026-09-03'),

-- Westlands Branch Sales
('WST_02', 'PROD_02', 14, 9100.00, '2026-08-28'),
('WST_02', 'PROD_05', 8, 2000.00, '2026-08-29'),
('WST_02', 'PROD_03', 10, 9000.00, '2026-08-31'),
('WST_02', 'PROD_04', 25, 7000.00, '2026-09-02'),
('WST_02', 'PROD_01', 18, 2700.00, '2026-09-03'),

-- Kasarani Branch Sales
('KSR_03', 'PROD_01', 22, 3300.00, '2026-08-29'),
('KSR_03', 'PROD_04', 15, 4200.00, '2026-08-30'),
('KSR_03', 'PROD_06', 40, 2600.00, '2026-09-01'),
('KSR_03', 'PROD_02', 7, 4550.00, '2026-09-03'),

-- Langata Branch Sales
('LNG_04', 'PROD_03', 5, 4500.00, '2026-08-30'),
('LNG_04', 'PROD_01', 16, 2400.00, '2026-08-31'),
('LNG_04', 'PROD_02', 12, 7800.00, '2026-09-02'),
('LNG_04', 'PROD_05', 10, 2500.00, '2026-09-03');


SELECT * FROM branches;
SELECT * FROM categories;
SELECT * FROM products;
SELECT * FROM transactions;


-- BRANCH TRANSACTION LOOK UP
SELECT
t.transaction_id,
p.product_name,
t.quantity_sold,
t.total_amount,
t.transaction_date
FROM transactions t
INNER JOIN products p ON t.product_id = p.product_id
WHERE t.branch_id = 'CBD_01'
ORDER BY t.total_amount DESC;

-- Multi-Table Branch & Product Join Query)
SELECT 
    t.transaction_id,
    t.transaction_date,
    b.branch_name,
    p.product_name,
    p.unit_price,
    t.quantity_sold,
    t.total_amount
FROM transactions t
INNER JOIN branches b ON t.branch_id = b.branch_id
INNER JOIN products p ON t.product_id = p.product_id;

-- branch revenue summary
SELECT 
    b.branch_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.quantity_sold) AS total_units_sold,
    SUM(t.total_amount) AS gross_revenue
FROM transactions t
INNER JOIN branches b ON t.branch_id = b.branch_id
GROUP BY b.branch_name
ORDER BY gross_revenue DESC;


-- Daily Sales Performance Trend
SELECT
t.transaction_date,
COUNT(t.transaction_id) AS daily_transactions,
SUM(t.quantity_sold) AS daily_units_sold,
SUM(t.total_amount) AS daily_revenue
FROM transactions t
GROUP BY t.transaction_date
ORDER BY t.transaction_date ASC;


-- Master Relational Data Extraction (SQL)

SELECT
t.transaction_id,
t.transaction_date,
b.branch_name,
c.category_name,
p.product_name,
p.unit_price,
t.quantity_sold,
t.total_amount
FROM transactions t
JOIN branches b ON t.branch_id = b.branch_id
JOIN products p ON t.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
ORDER BY t.transaction_date DESC;

-- ranking products by revenue inside each individual product category


SELECT
c.category_name,
p.product_name,
SUM(t.total_amount) AS total_revenue,
ROW_NUMBER() OVER (PARTITION BY c.category_name ORDER BY SUM(t.total_amount) DESC) AS row_num,
RANK() OVER (PARTITION BY c.category_name ORDER BY SUM(t.total_amount) DESC) AS item_rank,
DENSE_RANK() OVER(PARTITION BY c.category_name ORDER BY SUM(t.total_amount) DESC) AS dense_item_rank
FROM transactions t
JOIN products p ON t.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name,p.product_name;

-- looking at the chronological branch sales and preview the next transaction amount
SELECT
b.branch_name,
t.transaction_date,
t.total_amount AS current_sale_amount,
LEAD(t.total_amount,1) OVER (PARTITION BY b.branch_id ORDER BY t.transaction_date ASC) AS next_sale_amount,
(LEAD(t.total_amount,1) OVER (PARTITION BY b.branch_id ORDER BY t.transaction_date ASC) - t.total_amount) AS revenue_difference
FROM transactions t
JOIN branches b ON t.branch_id = b.branch_id
ORDER BY b.branch_name,t.transaction_date ASC;













