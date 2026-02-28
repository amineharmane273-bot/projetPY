CREATE DATABASE smart_inventory;
USE smart_inventory;

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL,
    quantity_in_stock INT DEFAULT 0
);

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO Products (last_name, category, price, quantity_in_stock) VALUES
('Laptop', 'Tech', 9000.00, 50),
('Phone', 'Tech', 5000.00, 80),
('Mouse', 'Tech', 150.00, 200),
('Keyboard', 'Tech', 200.00, 150),
('Monitor', 'Tech', 1200.00, 40),
('Tablet', 'Tech', 3000.00, 60),
('Printer', 'Tech', 900.00, 30),
('Camera', 'Tech', 2500.00, 25),
('Speaker', 'Tech', 400.00, 100),
('Headset', 'Tech', 350.00, 120);



INSERT INTO Customers (last_name, email) VALUES
('Amine', 'amine@gmail.com'),
('Ahmed', 'ahmed@gmail.com'),
('Omar', 'omar@gmail.com'),
('mohamed', 'mohamed@gmail.com'),
('Youssef', 'youssef@gmail.com'),
('Ali', 'ali@gmail.com');



INSERT INTO OrderItem (product_id, quantity) VALUES
(1, 1),
(2, 4),
(3, 5),
(4, 2),
(5, 2),
(6, 3);




INSERT INTO Orders (customer_id, order_date, orderitem_id) VALUES
(1, '2022-09-05', 1),
(2, '2023-05-07', 2),
(3, '2024-03-10', 3),
(4, '2025-01-15', 4),
(5, '2025-01-20', 5),
(6, '2025-02-01', 6);

