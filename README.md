#Online Sales Analysis Project

This project serves to help businesses streamline their operations in sales using smart software to boost productivity

#Classes

###Product
- Attributes: `name`, `price`, `quantity`
- Methods:
  - `display()` - Displays information about the product
  - `change_quantity()` - Updates the product's quantity

### ProductManager
- Attributes: List of products
- Methods:
  - `add_product()` - Adds a product to the list
  - `remove_product_by_name()` - Removes a product from the list
  - `display_products()` - Displays all products
  - `sum_value()` - Displays the total value of all products

### Cart
- Attribute: `cart_items` (list of products)
- Methods:
  - `add_item()` - Adds a product to the cart
  - `sum_cart_value()` - Displays the total value of products in the cart
  - `print()` - Displays the contents of the cart and their respective values

## Running the project

To start the software, you need to have Python installed. Simply run the `main.py` file from command prompt window with command: python main.py

