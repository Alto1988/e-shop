from django.urls import path

from .views import index, product_list

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:category>/', product_list, name='product_list'),
    path('<int:id>/<slug:slug>/', index, name='product_detail'),
]