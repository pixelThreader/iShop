from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category, name='category'),
    path('products/', views.products, name='products'),
    path('products/productcomment/', views.ipComment, name='productcomment'),
    path('upload-products/', views.uploadProduct, name='uploadproducts'),
    path('products/<str:slug>/', views.current_Product, name='curr_product'),
]