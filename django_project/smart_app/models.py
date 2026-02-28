from django.db import models

class Product(models.Model):
    # Attributs : id (auto), name, category, price, quantity_in_stock 
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Customer(models.Model):
    # Attributs : id (auto), name, email 
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    # Attributs : customer, order_date
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"

class OrderItem(models.Model):
    # Attributs : product, quantity 
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def get_subtotal(self):
        # Méthode métier pour calculer le sous-total d'un item de commande
        return self.product.price * self.quantity
