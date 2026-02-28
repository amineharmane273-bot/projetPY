"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # Product CRUD 
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    
    # Customer Registration
    path('customers/register/', views.customer_register, name='customer_register'),
    
    # Orders 
    path('orders/new/', views.create_order, name='create_order'),
    path('orders/history/', views.order_history, name='order_history'),
]