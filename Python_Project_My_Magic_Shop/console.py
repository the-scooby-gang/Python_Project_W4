import pdb
from models.products import Product
from models.suppliers import Supplier
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_repository.delete_all()
supplier_repository.delete_all()

supplier1 = Supplier()
supplier_repository.save(supplier1)

supplier2 = Supplier()
supplier_repository.save(supplier2)

supplier3 = Supplier()
supplier_repository.save(supplier3)

product1 = Product()
product_repository.save(product1)

product2 = Product()
product_repository.save(product2)

product3 = Product()
product_repository.save(product3)

product4 = Product()
product_repository.save(product4)

product5 = Product()
product_repository.save(product5)

pdb.set_trace()
