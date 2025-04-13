from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager=ProductManager()

product1=Product("Jacket",14800,45)
product2=Product("Shoe",12100,45)
product3=Product("Cap",800,45)
product4=Product("Ball",3210,45)
product5=Product("Sweater",4964,45)
product6=Product("Shirt",1800,45)
product7=Product("Jeans",3400,45)
product8=Product("Racket",7611,45)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)
manager.add_product(product5)
manager.add_product(product6)
manager.add_product(product7)
manager.add_product(product8)

print("Products in store:")
manager.display_products()

print(f"Total inventory value is:{manager.sum_value()}")

cart=Cart()
all_products=manager.products
random_products=random.sample(all_products,3)
for product in random_products:
    cart.add_item(product)

cart.print()
