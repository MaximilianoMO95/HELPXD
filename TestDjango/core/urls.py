from django.urls import path, include   
from django.contrib import admin
from .views import index
from .views import cerveza 
from .views import whisky
from .views import pisco 
from .views import ron
from .views import vodka  
from .views import carrito
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name="index"),  
    path('cerveza/', cerveza, name="cerveza"),
    path('whisky/', whisky, name="whisky"),
    path('pisco/', pisco, name="pisco"),
    path('ron/', ron, name="ron"),
    path('vodka/', vodka, name="vodka"),
    path('carrito/', carrito, name="carrito"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  

    
    
    
    
]