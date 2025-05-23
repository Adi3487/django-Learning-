from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth  import login 

def home(request):
    products= Product.objects.all()
    return render(request, "store/home.html", {"products": products})

def product_detail(request, pk):
    product= get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})
    #disinilah tampilan html yang kita buat di tampilkan ketika kita mengakses product_detail
    #yang di tampilkan adalah product yang kita ambil dari database menggunakan Django ORM
def add_to_cart(request, pk):
    product= get_object_or_404(Product, pk=pk)
    cart, created= Cart.objects.get_or_create(user=request.user)
    
    cart_item, created= CartItem.objects.get_or_create(cart=cart, product=product)
    if not created: #created == false artinya item sudah ada di dalam cart jadi kita hanya perlu menambah kan quantity nya saja 
        cart_item.quantity += 1
        cart_item.save()    
    #ketika kita ambil objek cart_item dari database menggunakan Django ORM,
    # maka objek itu sudah “mewakili” satu baris data dari tabel CartItem beserta semua field-nya, termasuk quantity.

    return redirect("cart_view")

def cart_view(request):
    cart, created= Cart.objects.get_or_create(user= request.user)
    return render(request, "store/cart.html", {"cart": cart})

def register(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect("home")
        
    else:
        form= UserCreationForm()
    return render(request, "store/register.html",{"form":form})

@login_required
def checkout(request):
    cart, created= Cart.objects.get_or_create(user= request.user) #Memastikan bahwa user punya keranjang belanja (Cart),
    #dan kalau keranjang itu kosong, maka tidak bisa lanjut checkout. 
    if not cart.items.exits():
        return redirect("cart_view")
    
    order= Order.objects.create(user=request.user)
    
    for item in cart.items.all():
        #Kurangi stok produk
        item.product.stock -= item.quantity
        item.product.save()
        
        #Buat OrderItem
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )
        
    #kosongkan Keranjang 
    cart.items.all().delete()
    return render(request,"store/checkout_succes.html",{"order":order})

@login_required
def remove_from_cart(request, item_id):
    item=get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect("cart_view")
    
    
