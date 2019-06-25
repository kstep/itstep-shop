from django.shortcuts import render, redirect
from django import views

# Create your views here.
from orders.forms import NewOrderForm
from orders.models import OrderItem


class OrderView(views.View):
    def get(self, request):
        return self.render_order_add_page(request,
                                          NewOrderForm())

    def post(self, request):
        # получить данные от пользователя
        data = request.POST

        # проверить данные на валидность
        form = NewOrderForm(data)

        # если всё валидно,
        # сохранить данные в базе
        if form.is_valid():
            cart = request.cart
            order = form.save()  # type: models.Order

            for cart_item in cart.items.all():
                order_item = OrderItem(
                    order=order,
                    item=cart_item.item,
                    amount=cart_item.amount)
                order_item.save()
            return redirect("item_list")
        else:
            return self.render_order_add_page(request, form)

    def render_order_add_page(self, request, form):
        context = {
            'form': form
        }
        return render(request, 'order_add.html',
                      context)
