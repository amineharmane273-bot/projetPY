from core.exceptions.exceptions import InvalidQuantityException, OutOfStockException, InvalidEmailException


class Product:
    def __init__(self, id, name, category, price, quantity_in_stock):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def add_stock(self, qty):
        if qty < 0:
            raise InvalidQuantityException("Quantity to add must be positive")
        self.quantity_in_stock += qty

    def remove_stock(self,qty):
        if qty < 0:
            raise InvalidQuantityException("Quantity to remove must be positive")
        if qty > self.quantity_in_stock:
            raise OutOfStockException("Not enough stock to remove")
        self.quantity_in_stock -= qty

    def get_value_in_stock(self):
        return self.price * self.quantity_in_stock 



class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def validate_email(self):
        if "@gmail.com" not in self.email:
            raise InvalidEmailException("Invalid email address")
        return True  


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.product=Product(product.id,product.name,product.category,product.price,product.quantity_in_stock)

    def get_subtotal(self):
        return self.product.price * self.quantity
    
class Order:
    def __init__(self, id, customer,order_date,items=None):
        self.id = id
        self.customer = customer
        self.order_date = order_date
        self.items = [OrderItem(items.product,items.quantity)] if items else []
    

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise InvalidQuantityException("Quantity must be positive")
        if quantity > product.quantity_in_stock:
            raise OutOfStockException("Not enough stock for this product")
        self.items.append(OrderItem(product, quantity))
        product.remove_stock(quantity)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_subtotal()
        return total 
    

if __name__ == "__main__":
      # Create product
    p1 = Product(1, "Laptop", "Tech", 9000, 70)
    p1.add_stock(30)
    p1.remove_stock(20)
    print("Value in stock:", p1.get_value_in_stock())
    # Create customer
    c1 = Customer(1, "Amine", "amine@gmail.com")
    c1.validate_email()
    # Create order
    order = Order(1, c1, "2022-09-05")
    order.add_item(p1, 2)
    print("Total:", order.calculate_total())
    orderitem = OrderItem(p1, 3)
    print("Subtotal:", orderitem.get_subtotal())

