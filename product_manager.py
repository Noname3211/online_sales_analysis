from product import Product

class ProductManager:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        self.products.append(product)
    def display_products(self):
        for product in self.products:
            product.display()
    def sum_value(self):
        return sum(product.quantity * product.price for product in self.products)
    def remove_product_by_name(self, name):
        original_len = len(self.products)
        self.products = [product for product in self.products if product.name != name]
        if len(self.products) < original_len:
            return original_len-len(self.products)
        else:
            return 0
    