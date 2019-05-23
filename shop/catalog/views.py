from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

# Create your views here.
from catalog.forms import ItemSortForm, ItemFilterForm
from catalog.models import Item


def item_list(request: HttpRequest):
    item_sort_form = ItemSortForm(request.GET)
    item_filter_form = ItemFilterForm(request.GET)

    filters = {
        k: v for (k, v) in
        item_filter_form.cleaned_data.items()
        if v is not None
    } if item_filter_form.is_valid() else {}

    return render(request, 'item_list.html',
                  {
                      'item_sort_form': item_sort_form,
                      'item_filter_form': item_filter_form,
                      'items': Item.objects
                                   .filter(**filters)
                                   .order_by(
                          (item_sort_form.cleaned_data['order_by'] or 'name')
                                         if item_sort_form.is_valid() else 'name')
                  })

def item_detail(request, pk):
    return render(request, 'item_detail.html',
                  {'item': get_object_or_404(Item, pk=pk)})