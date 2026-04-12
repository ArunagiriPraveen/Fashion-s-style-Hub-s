from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),

    # path('home/', views.home, name='home'),

    path('products/', views.product, name='product'),

    path('cart/', views.cart, name='cart'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

]