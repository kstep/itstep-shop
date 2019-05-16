from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import AddToCartForm
from cart.models import Cart, CartItem

# Create your views here.
from catalog.models import Item


def add_to_cart(request: HttpRequest):
    add_to_cart_form = AddToCartForm(request.GET)
    cart = get_cart(request.session)  # type: Cart

    if add_to_cart_form.is_valid():
        item = get_object_or_404(
            Item,
            pk=add_to_cart_form.cleaned_data['item_id'])
        add_item_to_cart(cart, item,
            add_to_cart_form.cleaned_data['amount'])

    return redirect('item_list')


def add_item_to_cart(cart: Cart,
                     item: Item,
                     amount: int = 1):
    cart_item = CartItem(
        cart=cart,
        item=item,
        amount=amount)
    cart_item.save()
    return cart_item


def get_cart(session):
    try:
        cart_id = session['cart_id']
        cart = Cart.objects.get(pk=cart_id)
    except (KeyError, Cart.DoesNotExist) as e:
        cart = Cart()
        cart.save()
        session['cart_id'] = cart.pk
    return cart

