from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    discount_price = models.FloatField(null=True, blank=True,)
    sold_out = models.BooleanField(default=False)
    description = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(blank=True, null=True, default="image.png")
    def __str__(self):
        return self.name

class Order(models.Model):
    #creating drop down menu in status selection

    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    quantity = models.FloatField(null=True, default=1)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    othername = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.address
