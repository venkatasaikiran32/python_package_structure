from ecommerce.product_management.services import add_product, list_products
from ecommerce.order_processing.services import create_order, list_orders
from ecommerce.product_management.models import Product
from ecommerce.order_processing.models import Order

def main():
    # Create some products
    p1 = Product(product_id=1, name="Laptop", price=999.99, quantity=10)
    p2 = Product(product_id=2, name="Smartphone", price=599.99, quantity=15)

    # Add products to the store
    add_product(p1)
    add_product(p2)

    # List products
    print("Products in store:")
    for product in list_products():
        print(product)

    # Create an order
    order1 = Order(order_id=101, product_id=1, quantity=2)
    create_order(order1)

    # List orders
    print("\nOrders placed:")
    for order in list_orders():
        print(order)

if __name__ == "__main__":
    main()
