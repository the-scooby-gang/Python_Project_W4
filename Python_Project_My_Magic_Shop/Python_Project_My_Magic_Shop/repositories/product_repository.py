from db.run_sql import run_sql
from models.products import Product
from models.suppliers import Supplier
import repositories.supplier_repository as supplier_repository

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buyer_cost, resale_price, supplier_id) VALUES (%s, %s, %s, %s, %s, %s"
    values = [product.name, product.description, product.stock_quantity, product.buyer_cost, product.resale_cost, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buyer_cost'], row['resale_price'], supplier)
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT* FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        supplier = supplier_repository.select(result['supplier_id'])
        product = Product(result['name'], result['description'], result['stock_quantity'], result['buyer_cost'], result['resale_price'], supplier)
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

    

