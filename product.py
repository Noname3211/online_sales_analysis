class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")
    def change_quantity(self,quantity):
        self.quantity=quantity