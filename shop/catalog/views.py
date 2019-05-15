from django.shortcuts import render, get_object_or_404

# Create your views here.
from catalog.models import Item


def item_list(request):
    return render(request, 'item_list.html', {'items': Item.objects.all()})

def item_detail(request, pk):
    return render(request, 'item_detail.html',
                  {'item': get_object_or_404(Item, pk=pk)})