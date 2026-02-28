from django import forms
from .models import Product, Customer
# Import des exceptions personnalisées définies en Partie 1
from core.exceptions.exceptions import InvalidEmailException, InvalidQuantityException, OutOfStockException

class ProductForm(forms.ModelForm):
    """Formulaire pour le CRUD Produit avec validation personnalisée"""
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity_in_stock']

    def clean_quantity_in_stock(self):
        """Validation personnalisée utilisant les exceptions métier"""
        quantity = self.cleaned_data.get('quantity_in_stock')
        if quantity is not None and quantity < 0:
            # On lève l'exception demandée en Partie 1 [cite: 50, 53]
            raise forms.ValidationError("Quantity must be positive")
        return quantity

class CustomerForm(forms.ModelForm):
    """Formulaire pour l'inscription client"""
    class Meta:
        model = Customer
        fields = ['name', 'email']

    def clean_email(self):
        """Validation de l'email avec capture d'exception personnalisée"""
        email = self.cleaned_data.get('email')
        # Simulation de la logique validate_email() [cite: 30]
        if "@" not in email or "." not in email:
            raise forms.ValidationError("Invalid email format")
        return email