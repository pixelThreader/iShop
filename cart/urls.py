from django.urls import path
from . import views

urlpatterns = [
    path('add-cart/', views.your_cart, name='your_cart'),
    path('my-cart/', views.my_cart, name='my_cart'),
    path('deleteitemcart/', views.deleteCartProduct, name='deleteitemcart'),
    path('updateCart/', views.updateCart, name='updateCart'),
]