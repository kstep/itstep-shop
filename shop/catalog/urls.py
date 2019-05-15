from django.urls import path

from catalog import views

urlpatterns = [
    path('item_list/', views.item_list, name='item_list'),
    path('item_detail/<int:pk>/', views.item_detail, name='item_detail')
]