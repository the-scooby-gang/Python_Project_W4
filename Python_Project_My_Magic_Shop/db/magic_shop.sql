DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS products;

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    stock_quantity INT,
    buyer_cost INT,
    resale_price INT
);

CREATE TABLE suppliers(
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    contact_name VARCHAR(255),
    human BOOLEAN,  
);