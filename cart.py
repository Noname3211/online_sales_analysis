class Cart:
    def __init__(self):
        self.cart_items=[]
    def add_item(self,product):
        self.cart_items.append(product)
    def sum_cart_value(self):
        return sum(item.price for item in self.cart_items)
    def print(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            for item in self.cart_items:
                print(f"{item.name} costing {item.price}")