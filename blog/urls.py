from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('post/', views.post_blogs, name='posts'),
    path('search/', views.post_search, name='posts'),
]