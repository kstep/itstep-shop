from django import template

register = template.Library()

@register.filter(name="instock")
def in_stock(value, arg="In Stock|Out of Stock"):
    '''
    Filter function, returns instock or outofstock
    depending in amount items.

    :param value: any object with numeric count field
    :param arg: pipe-separated string with two parts
    :return: string, one of arg parts
    '''
    arg = arg.split('|')
    return arg[0] if value.count > 0 else arg[1]
