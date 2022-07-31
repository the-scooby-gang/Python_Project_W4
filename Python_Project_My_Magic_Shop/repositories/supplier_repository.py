from db.run_sql import run_sql
from models.products import Product
from models.suppliers import Supplier
import repositories.product_repository as product_repository

def save(supplier):
    sql = "INSERT INTO suppliers(company_name, contact_name, human) VALUES (%s, %s, %s) RETURNING *"
    values = [supplier.company_name, supplier.contact_name, supplier.human]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier

def select_all():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)
    for row in results:
        supplier = Supplier(row['company_name'], row['contact_name'], row['human'])
        suppliers.append(supplier)

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        supplier = Supplier(result['company_name'], result['contact_name'], result['human'])
    return supplier

def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


