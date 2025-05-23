from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views 
from . import views 



urlpatterns =[
    path("",views.home, name="home"), #tampilan utama yang user lihat kettika mengakses website kita 
    path("product/<int:pk>", views.product_detail, name="product_detail" ),
    # tampilan kedua yang user lihat ketika mengakses product
    path("add_to_cart/<int:pk>", views.add_to_cart, name="add_to_cart"),
    #name="product_detail" adalah nama yang kita berikan untuk memudahkan kita untuk mengakses url ini di dalam template
    path("cart/", views.cart_view, name="cart_view"),
    path("login/", auth_views.LoginView.as_view(template_name="store/login.html"), name="login"),
    path("logout/",auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register,name="register"),
    path("remove-from-cart/<int:item_id>/",views.remove_from_cart, name="remove_from_cart"),
]   
