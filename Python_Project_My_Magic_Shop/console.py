import pdb
from models.products import Product
from models.suppliers import Supplier
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_repository.delete_all()
supplier_repository.delete_all()

supplier1 = Supplier("Witches Coven Sunnydale", "Willow Rosenberg" , True)
supplier_repository.save(supplier1)

supplier2 = Supplier("Sunnydale High School", "Prinicipal Snyder", True)
supplier_repository.save(supplier2)

supplier3 = Supplier("Crawford Mansion", "William The Bloody", False)
supplier_repository.save(supplier3)

supplier_repository.select_all()

product1 = Product("Love Potion", "Add this potion to your crushes to make them fall in love with you. Warning! Dangerous! Please consider also buying the love potion antidote", 10, 20, 400, supplier1)
product_repository.save(product1)

product2 = Product("Magic for Beginners", "Book to dabble in the basic arts of magic (Classes available on request)", 1, 30, 50, supplier2)
product_repository.save(product2)

product3 = Product("Ring of Armara", "Magical ring that grants vampires complete invulnerability to all the usual weaknesses", 0, 0, 15000, supplier3)
product_repository.save(product3)

product4 = Product("Ancient Mummy Hand", "Undead Mummy Hand, useful for prosperity spells", 1, 200, 430, supplier3)
product_repository.save(product4)

product5 = Product("Burba Weed", "Stir into blood to make it hot and spicy", 16, 5, 15, supplier3)
product_repository.save(product5)

pdb.set_trace()

