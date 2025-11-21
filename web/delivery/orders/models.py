import uuid
from decimal import Decimal
from django.db import models

class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    client_phone_number = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def total_price(self) -> Decimal:
        result = 0
        
        # sum of all items prices in the order
        for item in self.items.all():
            result += item.price_after_tax
        
        # apply discount
        result = result - (result * self.discount)
        
        return result

    class Meta:
        ordering = ['updated_at']
    
    def __str__(self):
        return f"Order {self.uuid} - {self.total_price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    iva_tax = models.DecimalField(max_digits=3, decimal_places=2, default=0.23)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def price_befor_tax(self):
        return self.unit_price * self.quantity
    
    @property
    def price_after_tax(self):
        return self.price_befor_tax + (self.price_befor_tax * self.iva_tax)


    class Meta:
        ordering = ['updated_at']
    
    def __str__(self):
        return f"{self.name} - {self.unit_price} {self.quantity} x"

