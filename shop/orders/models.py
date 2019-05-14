from django.db import models

# Create your models here.
from catalog.models import ItemAmount


class OrderItem(ItemAmount):
    order = models.ForeignKey('Order',
                              on_delete=models.CASCADE,
                              related_name='items')


class Order(models.Model):
    shipping = models.TextField()
