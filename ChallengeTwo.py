#Challenge 2: Refactoring with Composition 

class Product:
    def __init__(self, name, price, supplier):
        self.name = name
        self.price = price
        self.supplier = supplier

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Supplier: {self.supplier.name if self.supplier else 'Unknown'}"


class Supplier:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Supplier: {self.name}, Contact: {self.contact_info}"


class Inventory:
    def __init__ (self):
        self.stock = {}

    def restock(self, product, quantity):
        if quantity <= 0:
            print("Restock quantity must be positive.")
            return
        elif product.supplier is None:
            print(f"Cannot restock {product.name} as it has no supplier.")
        elif product in self.stock:
            self.stock[product] += quantity
            print(f"Restocked {quantity} units of {product.name}. New stock: {self.stock[product]}")
        else:
            self.stock[product] = quantity
            print(f"Added {product.name} to inventory with initial stock of {quantity}.")
    
    def print_stock(self):
        print("Current Inventory Stock: ")
        for product, quantity in self.stock.items():
            print(f"Product: {product.name}, Stock: {quantity}")

    def __str__(self):
        return f"Inventory with {len(self.stock)} products."


#Examples
supplier1 = Supplier("CarParts Inc.", "contact@carparts.com")
product1 = Product("Fender", 2000.99, supplier1)
product2 = Product("Front Bumper", 200.00, supplier1)

inventory = Inventory()
inventory.restock(product1, 10)
inventory.restock(product2, 25)
inventory.print_stock()
