from django.contrib import admin

# Register your models here.
from cart import models


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    pass