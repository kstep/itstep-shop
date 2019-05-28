from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin

from cart.models import Cart


class CartMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        request.cart = self.get_cart(request.session)
        response = self.get_response(request)
        return response

    @staticmethod
    def get_cart(session):
        try:
            cart_id = session['cart_id']
            cart = Cart.objects.get(pk=cart_id)
        except (KeyError, Cart.DoesNotExist) as e:
            cart = Cart()
            cart.save()
            session['cart_id'] = cart.pk
        return cart