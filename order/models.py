# models.py
from django.db import models
from menu.models import MenuItem
from accounts.models import CustomUser


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem') 
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for Order #{self.order.id}"

