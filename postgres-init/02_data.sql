-- data.sql
INSERT INTO users (name, email, address_state_code, address_city) VALUES
('Alice Smith', 'alice@example.com', 'NY', 'New York'),
('Bob Johnson', 'bob@example.com', 'CA', 'Los Angeles'),
('Charlie Brown', 'charlie@example.com', 'TX', 'Houston'),
('Dana White', 'dana@example.com', 'FL', 'Orlando'),
('Eve Black', 'eve@example.com', 'WA', 'Seattle');

INSERT INTO products (name, price_dollars) VALUES
('Pizza', 12.50),
('Sushi', 9.99),
('Burger', 5.99),
('Salad', 4.50),
('Tacos', 3.99);

INSERT INTO drivers (name, address_state_code, address_city) VALUES
('Sam Tyler', 'NY', 'New York'),
('Joan Baez', 'CA', 'San Francisco'),
('Liam Neeson', 'TX', 'Austin'),
('Nora Jones', 'FL', 'Miami'),
('Tina Turner', 'WA', 'Seattle');

INSERT INTO orders (user_id, driver_id, product_id, quantity, ordered_at, delivered_at, status) VALUES
(1, 1, 1, 2, '2024-04-20 14:00:00-04', '2024-04-20 15:30:00-04', 'Delivered'),
(2, 2, 2, 1, '2024-04-20 15:05:00-04', '2024-04-20 16:20:00-04', 'Delivered'),
(3, 3, 3, 3, '2024-04-21 12:30:00-04', '2024-04-21 13:00:00-04', 'Delivered'),
(4, 4, 4, 1, '2024-04-22 18:15:00-04', '2024-04-22 19:00:00-04', 'Delivered'),
(5, 5, 5, 5, '2024-04-22 20:00:00-04', NULL, 'Pending'),
(1, 2, 5, 2, '2024-04-23 10:00:00-04', NULL, 'Pending'),
(2, 1, 3, 2, '2024-04-23 09:15:00-04', '2024-04-23 10:40:00-04', 'Delivered'),
(3, 4, 1, 1, '2024-04-24 11:00:00-04', NULL, 'Pending'),
(4, 3, 2, 4, '2024-04-24 13:20:00-04', '2024-04-24 14:45:00-04', 'Delivered'),
(5, 2, 4, 1, '2024-04-25 15:35:00-04', '2024-04-25 16:50:00-04', 'Delivered'),
(1, 5, 5, 3, '2024-04-25 17:05:00-04', '2024-04-25 18:30:00-04', 'Delivered'),
(2, 4, 1, 1, '2024-04-26 08:30:00-04', NULL, 'Pending'),
(3, 3, 2, 2, '2024-04-26 09:45:00-04', '2024-04-26 11:00:00-04', 'Delivered'),
(4, 2, 3, 3, '2024-04-27 12:00:00-04', '2024-04-27 12:35:00-04', 'Delivered'),
(5, 1, 4, 2, '2024-04-27 14:20:00-04', '2024-04-27 15:45:00-04', 'Delivered'),
(1, 5, 5, 2, '2024-04-28 16:10:00-04', NULL, 'Pending'),
(2, 4, 1, 4, '2024-04-28 17:25:00-04', '2024-04-28 18:50:00-04', 'Delivered'),
(3, 2, 3, 1, '2024-04-29 19:00:00-04', '2024-04-29 20:15:00-04', 'Delivered'),
(4, 3, 2, 2, '2024-04-30 20:40:00-04', '2024-04-30 21:55:00-04', 'Delivered'),
(5, 1, 4, 3, '2024-05-01 22:05:00-04', NULL, 'Pending');

