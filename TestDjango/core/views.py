from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingCart, Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    return render(request, 'core/index.html')

def cerveza(request):
    return render(request, 'core/cerveza.html')

def whisky(request):
    return render(request, 'core/whisky.html')

def pisco(request):
    return render(request, 'core/pisco.html')

def ron(request):
    return render(request, 'core/ron.html')

def vodka(request):
    return render(request, 'core/vodka.html')




def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 1)

        product = get_object_or_404(Product, pk=product_id)

       
        shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)

       
        shopping_cart.add_to_cart(product, quantity)

    return redirect('carrito')  


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index') 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
    return render(request, 'core/login.html', {'form': AuthenticationForm()})

@login_required
def carrito(request):
    user = request.User
    
   
    shopping_cart, created = ShoppingCart.objects.get_or_create(User=user)
    
    
    cart_items = shopping_cart.cartitem_set.all()

    context = {
        'cart_items': cart_items,
    }
    return render(request, 'carrito.html', context)