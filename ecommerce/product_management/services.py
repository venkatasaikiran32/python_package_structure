from .models import Product

# Example in-memory product store
product_store = {}

def add_product(product):
    if product.product_id in product_store:
        raise ValueError("Product with this ID already exists.")
    product_store[product.product_id] = product

def get_product(product_id):
    return product_store.get(product_id)

def list_products():
    return list(product_store.values())
