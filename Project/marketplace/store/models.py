from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model):
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    #bagian ini langsung terpanggil ketika kita memanggil class category karena kita sudah mendefinisikan __str__ di dalam class category
    
    #Untuk mengakses name di dalam class category kita harus mengakses category.name 
class Product(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to="products/", blank=True, null=True)
    #cascade adalah jika kita menghapus category maka product yang ada di dalam category tersbut juga akan terhapus 
    def __str__(self):
        return self.name  #memasukkan name ke dalam def yang mengubah string agar name bisa di baca dengan mudah oleh user
    #dan yang lain tidak di masukkan karena yang lain mudah untuk di baca oleh user 
    #tapi  jika kita mau kita bisa memasukkan yang lain juga seperti price ataupun yang lain  return f"{self.name} - Rp{self.price}"
    #jadi memasukkan memasukkan variable ke dalam string berfungsi untuk memudahkan user untuk membaca variable tersebut 
    #bagian ini langsung terpanggil ketika kita memanggil class product karena kita sudah mendefinisikan __str__ di dalam class product 

class Order(models.Model): 
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default= False)
    #jika completed = True maka order sudah di bayar
    def __str__(self):
        return f"order {self.id} by {self.user.username}" #mengakses username dari user yang ada di dalam order 
    #user secara default berisi dari id, username,password, dan email 
    #sedangkan id sudah otomatis di buat oleh django 
    
#next learning 
#class Category(models.Model):
    #name = models.CharField(max_length=100)
#class Product(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)


# class Student(models.Model):
#     name = models.CharField(max_length=100)
# class Kursus(models.Model):
#     title = models.CharField(max_length=100)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)


    
class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE,related_name="items")
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1 )
    
    def __str__(self):
        return f"{self.quatity} of {self.product.name}" 
    #kita menggunakan product.name untuk mengakses name yang ada di dalam product
    
    # "." berfungsi untuk mengakses data yang ada di dalam product dan untuk mereferensikan ke product yang ada di dalam orderitem 
    
class Cart(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s Cart"
    
class CartItem(models.Model):
    cart= models.ForeignKey(Cart, on_delete= models.CASCADE, related_name= "items")
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default= 1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name }" 