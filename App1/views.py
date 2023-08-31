from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, CartItem, Cart, Category

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id= product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item = CartItem(cart=cart, product=product, quantity=1)
        cart_item.save()
        return redirect('product-list')

class CartView(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(cart__user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
        }
        return render(request, 'cart.html', context)

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if cart_item.cart.user == request.user:
        cart_item.delete()
    return redirect('cart')

def update_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if cart_item.cart.user == request.user:
        new_quantity = int(request.POST['quantity'])
        cart_item.quantity = new_quantity
        cart_item.save()
    return redirect('cart')


def checkout(request):
        if request.method == 'POST':
            return redirect('order-success')
        return render(request, 'checkout.html')


class OrderSuccessView(View):
    def get(self, request):
        return render(request, 'order_success.html')

def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def products_by_category_view(request ,category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products_by_category.html', {'category': category, 'products': products})

def about_view(request):
    return render(request, 'about.html')


