from django.urls import path
from . import views

urlpatterns = [
    path('our-privacy-and-policy', views.policy, name='ourpolicy'),
    path('our-terms-and-conditions', views.tandc, name='ourtermsandconditions'),
    path('support', views.support, name='support'),
]
