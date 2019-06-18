from django.db import models

# Create your models here.
from django.utils import timezone

from catalog.models import ItemAmount


class InvalidOrderStateError(RuntimeError):
    def __init__(self, old_state, new_state):
        self.old_state = old_state
        self.new_state = new_state

    def __str__(self):
        return 'Invalid order state transition: ' + \
            f'{self.old_state} -> {self.new_state}'


class OrderItem(ItemAmount):
    order = models.ForeignKey('Order',
                              on_delete=models.CASCADE,
                              related_name='items')


class PaymentType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    tel = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TextField()
    payment_type = models.ForeignKey(PaymentType,
                                     on_delete=models.CASCADE)

    STATES = [
        ('new', 'New order'),
        ('in_review', 'In review'),
        ('accepted', 'Order accepted'),
        ('rejected', 'Order rejected'),
        ('shipping', 'Shipping order'),
        ('delivered', 'Order delivered'),
        ('dropped', 'Order delivery failed')
    ]

    state = models.CharField(max_length=20,
                             choices=STATES,
                             default='new')

    def review(self):
        if self.state == 'new':
            self.state = 'in_review'
        else:
            raise InvalidOrderStateError(self.state, 'in_review')

    def accept(self):
        if self.state == 'in_review':
            self.state = 'accepted'
        else:
            raise InvalidOrderStateError(self.state, 'accepted')

    def reject(self):
        if self.state == 'in_review':
            self.state = 'rejected'
        else:
            raise InvalidOrderStateError(self.state, 'rejected')

    def ship(self):
        if self.state == 'accepted':
            self.state = 'shipping'
        else:
            raise InvalidOrderStateError(self.state, 'shipping')

    def deliver(self):
        if self.state == 'shipping':
            self.state = 'delivered'
        else:
            raise InvalidOrderStateError(self.state, 'delivered')

    def drop(self):
        if self.state == 'shipping':
            self.state = 'dropped'
        else:
            raise InvalidOrderStateError(self.state, 'dropped')