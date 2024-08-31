import unittest
from ecommerce.product_management.models import Product
from ecommerce.product_management.services import add_product
from ecommerce.order_processing.models import Order
from ecommerce.order_processing.services import create_order, get_order, list_orders

class TestOrderProcessing(unittest.TestCase):
    def setUp(self):
        # Clear product and order store
        from ecommerce.product_management.services import product_store
        from ecommerce.order_processing.services import order_store
        product_store.clear()
        order_store.clear()
    
    def test_create_order(self):
        p = Product(product_id=1, name="Test Product", price=10.99, quantity=100)
        add_product(p)
        order = Order(order_id=101, product_id=1, quantity=2)
        create_order(order)
        self.assertEqual(get_order(101), order)

    def test_list_orders(self):
        p = Product(product_id=1, name="Product", price=10.00, quantity=10)
        add_product(p)
        order1 = Order(order_id=101, product_id=1, quantity=2)
        order2 = Order(order_id=102, product_id=1, quantity=1)
        create_order(order1)
        create_order(order2)
        orders = list_orders()
        self.assertEqual(len(orders), 2)

if __name__ == '__main__':
    unittest.main()
