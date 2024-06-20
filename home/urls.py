from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('settings/', views.settings, name='settings'),
    path('contact/', views.contact, name='contact'),
]