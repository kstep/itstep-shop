from django.contrib import admin

# Register your models here.
from catalog import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    pass
