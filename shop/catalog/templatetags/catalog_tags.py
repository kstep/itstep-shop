from django import template
from django.utils.safestring import SafeText

register = template.Library()

@register.inclusion_tag('tags/add_to_cart_form.html')
def add_to_cart_form(item):
    return {'item': item}

@register.simple_tag()
def add_to_cart_form_simple(item):
    return SafeText(f'''
<form action="/add_to_cart" method="GET">
    <input name="item_id" type="hidden" value="{item.pk}" />
    <input name="amount" type="number"
           value="1" min="1"
           class="amount" />
    <input type="submit" value="В корзину" />
</form>
    ''')