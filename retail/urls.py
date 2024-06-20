from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.Checkout, name='curr_product_Checkout'),
    path('checkoutThis/icecream/', views.ToCheckoutOne, name='curr_product_ToCheckoutOne'),
    path('checkoutThis/', views.Checkout_one, name='curr_product_Checkout_one'),
    path('checkoutThis/paymentThis', views.payment_one, name='curr_product_Payment_one'),
    path('payments/', views.payment, name='curr_product_payment'),
    path('my-cupons/', views.cupons, name='cupons'),
    path('generate-cupons/', views.GenCupons, name='generatecupons'),
    path('remove-cupons/', views.TrashCupons, name='removecupons'),
    path('your_invoice/', views.invoice, name='invoice'),
]