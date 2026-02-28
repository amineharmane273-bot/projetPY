from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Customer, Order, OrderItem
# Import des exceptions personnalisées de la Partie 1 
from core.exceptions.exceptions import OutOfStockException, InvalidQuantityException, InvalidEmailException

def create_order(request):
    """Fonction pour créer une commande et gérer le stock en même temps"""
    products = Product.objects.all()
    customers = Customer.objects.all()
    
    if request.method == "POST":
        try:
            product_id = request.POST.get('product_id')
            qty = int(request.POST.get('quantity'))
            customer_id = request.POST.get('customer_id')
            
            product = Product.objects.get(id=product_id)
            
            # Utilisation de l'exception personnalisée pour vérifier le stock et la validité de la quantité
            if qty > product.quantity_in_stock:
                raise OutOfStockException(f"Stock insuffisant pour {product.name}")
            
            if qty <= 0:
                raise InvalidQuantityException("La quantité doit être positive")

            # Création de la commande
            customer = Customer.objects.get(id=customer_id)
            order = Order.objects.create(customer=customer)
            OrderItem.objects.create(order=order, product=product, quantity=qty)
            
            # Mise à jour du stock
            product.quantity_in_stock -= qty
            product.save()
            
            messages.success(request, "Commande validée avec succès !")
            return redirect('order_history')

        except (OutOfStockException, InvalidQuantityException) as e:
            # Message d'erreur convivial pour l'utilisateur 
            messages.error(request, str(e))
            
    return render(request, 'inventory/order_form.html', {
        'products': products, 
        'customers': customers
    })

def order_history(request):
    """Affiche l'historique des commandes """
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'inventory/order_history.html', {'orders': orders})


def product_list(request):
    """Affiche la liste de tous les produits """
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_create(request):
    """Ajoute un produit avec validation """
    if request.method == "POST":
        try:
            qty = int(request.POST.get('quantity_in_stock'))
            if qty < 0:
                raise InvalidQuantityException("La quantité doit être positive ou nulle")
            
            Product.objects.create(
                name=request.POST.get('name'),
                category=request.POST.get('category'),
                price=request.POST.get('price'),
                quantity_in_stock=qty
            )
            messages.success(request, "Produit ajouté !")
            return redirect('product_list')
        except InvalidQuantityException as e:
            messages.error(request, str(e)) # Message d'erreur convivial 
            
    return render(request, 'inventory/product_form.html')

def customer_register(request):
    """Enregistre un nouveau client """
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')

            # Validation simple (peut utiliser la méthode validate_email de la Partie 1)
            if "@" not in email:
                raise InvalidEmailException("Format d'email invalide ")

            Customer.objects.create(name=name, email=email)
            messages.success(request, f"Bienvenue {name} !")
            return redirect('product_list')
            
        except InvalidEmailException as e:
            messages.error(request, str(e)) # Message d'erreur convivial pour l'utilisateur
            
    return render(request, 'inventory/customer_form.html')
