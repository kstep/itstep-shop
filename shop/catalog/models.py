from django.db import models

# Create your models here.
from django.db.models import F


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.PositiveIntegerField()

    def __str__(self):
        return "Item #{} {}, price {}".format(self.pk, self.name, self.price)


class ItemContainer:
    def add_item(self, item: Item, amount: int = 1):
        if self.items.filter(item=item)\
                .update(amount=F('amount') + amount) == 0:
            # c_item = CItem(...
            container = self.__class__.__name__.lower()
            c_item = self.items.model(
                item=item,
                amount=amount,
                **{container: self})
            c_item.save()


class ItemAmount(models.Model):
    class Meta:
        abstract = True

    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='+')

    amount = models.PositiveIntegerField()

    @property
    def total_price(self):
        return self.item.price * self.amount

