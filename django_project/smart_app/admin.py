from django.contrib import admin
from .models import Product, Customer, Order, OrderItem

# Enregistrement des modèles pour l'interface Admin [cite: 106]
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Permet de voir les articles directement dans la commande [cite: 108]
    inlines = [OrderItemInline]
    list_display = ['id', 'customer', 'order_date']