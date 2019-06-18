from django.contrib import admin

# Register your models here.
from orders import models
from orders.models import InvalidOrderStateError


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    exclude = ['state']
    actions = ['review',
               'accept',
               'reject',
               'ship',
               'deliver',
               'drop']

    def transfer_state(self, newstate, queryset):
        for order in queryset:
            try:
                method = getattr(order, newstate)
                method()
            except InvalidOrderStateError:
                pass
            order.save()

    def review(self, request, queryset):
        self.transfer_state('review', queryset)
    def accept(self, request, queryset):
        self.transfer_state('accept', queryset)
    def reject(self, request, queryset):
        self.transfer_state('reject', queryset)



@admin.register(models.PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    pass