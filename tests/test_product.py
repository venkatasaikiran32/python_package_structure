import unittest
from ecommerce.product_management.models import Product
from ecommerce.product_management.services import add_product, get_product, list_products

class TestProductManagement(unittest.TestCase):
    def setUp(self):
        # Clear product store
        from ecommerce.product_management.services import product_store
        product_store.clear()
    
    def test_add_and_get_product(self):
        p = Product(product_id=1, name="Test Product", price=10.99, quantity=100)
        add_product(p)
        self.assertEqual(get_product(1), p)

    def test_list_products(self):
        p1 = Product(product_id=1, name="Product 1", price=20.00, quantity=10)
        p2 = Product(product_id=2, name="Product 2", price=30.00, quantity=20)
        add_product(p1)
        add_product(p2)
        products = list_products()
        self.assertEqual(len(products), 2)

if __name__ == '__main__':
    unittest.main()
