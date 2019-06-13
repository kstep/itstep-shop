from django.db import models

# Create your models here.
from django.utils import timezone

from catalog.models import ItemAmount


class OrderItem(ItemAmount):
    order = models.ForeignKey('Order',
                              on_delete=models.CASCADE,
                              related_name='items')


class PaymentType(models.Model):
    name = models.CharField(max_length=200)

class Order(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    tel = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TextField()
    payment_type = models.ForeignKey(PaymentType,
                                     on_delete=models.CASCADE)
    state = models.CharField(max_length=20)



