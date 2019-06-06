from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from cart.forms import AddToCartForm
# Create your views here.
from catalog.models import Item


class CartView(View):
    def post(self, request):
        add_to_cart_form = AddToCartForm(request.POST)
        cart = request.cart

        if add_to_cart_form.is_valid():
            item = get_object_or_404(
                Item,
                pk=add_to_cart_form.cleaned_data['item_id'])
            cart.add_item(item,
                          add_to_cart_form.cleaned_data['amount'])

        return redirect('item_list')

    def get(self, request):
        return render(request, 'cart_list.html', {
            'cart': request.cart
        })




