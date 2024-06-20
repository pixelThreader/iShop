from django.contrib import admin
from .models import AllProducts, Category, Flavour, ProductComment, CommentLike, CommentDislike

# Register your models here.

admin.site.register((AllProducts, Category, Flavour, ProductComment, CommentLike, CommentDislike))