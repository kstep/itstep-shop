from django.contrib import messages
from django.contrib.messages import add_message
from django.core.mail import mail_admins, send_mail, EmailMessage
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
                order.add_item(cart_item.item, cart_item.amount)

            cart.items.all().delete()

            message = EmailMessage(
                from_email='robot@shop.com',
                subject='Получен новый заказ',
                cc=[order.email],
                to=['admin@shop.com', 'manager@shop.com'],
                body=f'Получен новый заказ: id={order.pk}, от {order.email}',
                attachments=[
                    ('order.txt', f'Заказ {order.pk} ...', 'text/plain')
                ]
            )
            message.send()

            add_message(request, messages.INFO, "Заказ успешно создан")

            return redirect("item_list")
        else:
            return self.render_order_add_page(request, form)

    def render_order_add_page(self, request, form):
        context = {
            'form': form
        }
        return render(request, 'order_add.html',
                      context)
