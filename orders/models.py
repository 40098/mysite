from django.db import models
from django.contrib.auth.models import User


class Customer (models.Model):
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    company = models.CharField(max_length=40, blank=True)
    email = models.CharField(max_length=40, blank=True)
    phone = models.IntegerField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.company)!=0:
            return f"{self.company}"
        elif len(self.last_name)!=0:
            return f"{self.last_name}"
        else:
            return "Undefind"

class Product (models.Model):
    code = models.IntegerField(unique=True)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.code}"


class Order (models.Model):
    statusChoices = (
        (0, 'active'),
        (1, 'done'),
        (1, 'on hold'),
        (2, 'stuck'),
    )
    code = models.CharField(unique=True, max_length=20)
    worker = models.ManyToManyField(User)
    customer = models.ManyToManyField(Customer)
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=40)
    status = models.IntegerField(default=0, choices= statusChoices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"





