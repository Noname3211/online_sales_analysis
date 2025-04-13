from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager=ProductManager()

product1=Product("Sardine",14800,445)
product2=Product("Shark",12100,7)
product3=Product("Cat",800,45)
product4=Product("Car",3210,15)
product5=Product("Snake",4964,38)
product6=Product("Lyon",1800,4)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)
manager.add_product(product5)
manager.add_product(product6)


cart=Cart()
all_products=manager.products
random_products=random.sample(all_products,3)
for product in random_products:
    cart.add_item(product)

