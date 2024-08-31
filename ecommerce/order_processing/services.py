from ecommerce.product_management.services import get_product
from .models import Order

# Example in-memory order store
order_store = {}

def create_order(order):
    product = get_product(order.product_id)
    if not product:
        raise ValueError("Product not found.")
    if order.quantity > product.quantity:
        raise ValueError("Insufficient product quantity.")
    
    order_store[order.order_id] = order
    product.quantity -= order.quantity
    return order

def get_order(order_id):
    return order_store.get(order_id)

def list_orders():
    return list(order_store.values())
