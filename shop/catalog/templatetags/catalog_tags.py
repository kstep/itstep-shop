from django import template
from django.utils.safestring import SafeText

register = template.Library()

@register.inclusion_tag('tags/add_to_cart_form.html')
def add_to_cart_form(item):
    return {'item': item}
