DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers(
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    contact_name VARCHAR(255),
    human BOOLEAN
);

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buyer_cost INT,
    resale_price INT,
    supplier_id INT NOT NULL REFERENCES suppliers(id)

);

