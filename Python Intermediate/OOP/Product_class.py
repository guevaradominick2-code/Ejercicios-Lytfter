class Product():
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

class Inventory():
    def __init__(self,):
        self.products_list = []

    def add_product(self, product):
        self.products_list.append(product)

    def inventory_display(self):
        if not self.products_list:
            print("Inventory is empty")
        else:
            print(f"{'Product':<12}{'Price':<10}{'Quantity':<10}")
            print("-" * 32)

            for product in self.products_list:
                print(f"{product.product_name:<12}{product.price:<10}{product.quantity:<10}")
            
    def total_inventory_value(self):
        total = 0
        
        for product in self.products_list:
            total += product.price * product.quantity
        return total
    
product_1 = Product("Mouse", 2500, 10)
product_2 = Product("Case", 75000, 5)
product_3 = Product("Keyboard", 5000, 20)
product_4 = Product("RAM", 980000, 4)
product_5 = Product("Monitor", 100000, 10)

storage = Inventory()
storage.add_product(product_1)
storage.add_product(product_2)
storage.add_product(product_3)
storage.add_product(product_4)
storage.add_product(product_5)

storage.inventory_display()

print(f"The total value of the inventory is: {storage.total_inventory_value():,}")

