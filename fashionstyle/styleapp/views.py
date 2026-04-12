from django.shortcuts import render, redirect
from .models import Product, Cart
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def master(request):
    return render (request, 'master.html')

def home(request):
    return render(request, 'home.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

# views.py


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.save()

    return redirect('cart')
    return redirect('product')


# cart in views
@login_required
def cart(request):
    cart_items = Cart.objects.all()

    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

# login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user_login = authenticate(request, username=username, password=password)

        if user_login:
            login(request, user_login)
            messages.success(request, "Your's Login was Successfull, Let's carry on about your Work....")
            return redirect('product')

        else:
            messages.error(request, "Your's Login was UnSuccessfull, Try agian Later")

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Thank you!!! Logged out Successfully,....")
    return redirect('login')

