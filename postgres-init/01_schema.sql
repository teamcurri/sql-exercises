-- schema.sql
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    address_state_code VARCHAR(2),
    address_city VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price_dollars DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS drivers (
    driver_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address_state_code VARCHAR(2),
    address_city VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    driver_id INT REFERENCES drivers(driver_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    ordered_at TIMESTAMPTZ,
    delivered_at TIMESTAMPTZ,
    status VARCHAR(50)
);
