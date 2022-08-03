import unittest
from models.products import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Love Potion", "make everyone love you", 1, 1, 2, "Willow")

    def test_product_name(self):
        product = self.product.name
        self.assertEqual("Love Potion", product)