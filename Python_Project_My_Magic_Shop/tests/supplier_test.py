import unittest
from models.suppliers import Supplier

class TestSupplier(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("Love Potion", "Willow", False)

    def test_product_name(self):
        supplier = self.supplier.company_name
        self.assertEqual("Love Potion", supplier)

    
