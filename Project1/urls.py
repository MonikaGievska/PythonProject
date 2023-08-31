"""
URL configuration for Project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from App1.views import product_list_view, product_detail_view, AddToCartView, CartView, OrderSuccessView, checkout, update_cart, remove_from_cart, home_view, category_list_view, products_by_category_view,about_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list_view, name='product-list'),
    path('products/<int:product_id>/', product_detail_view, name='product-detail'),
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove-from-cart'),
    path('cart/update/<int:cart_item_id>/', update_cart, name='update-cart'),
    path('order-success/', OrderSuccessView.as_view(), name='order-success'),
    path('checkout/', checkout, name='checkout'),
    path('',home_view, name='home'),
    path('categories/', category_list_view, name='category-list'),
    path('products/category/<int:category_id>/', products_by_category_view, name='products-by-category'),
    path('about/', about_view, name='about'),
]