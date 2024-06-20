"""
URL configuration for iShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import urls as home_URLS
from blog import urls as blog_URLS
from retail import urls as retail_URLS
from OurUsersAuth import urls as MyUsers
from products import urls as Stock
from cart import urls as Cart
from iShopLegalDocuments import urls as LGDocs

# Some Primary changes in admin panel
admin.site.site_header = 'iShop e-Commerce Administration'
admin.site.site_title = 'iShop'
admin.site.index_title = 'iShop Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_URLS)),
    path('blog/', include(blog_URLS)),
    path('retail/', include(retail_URLS)),
    path('stock/', include(Stock)),
    path('cart/', include(Cart)),
    path('authenticateOurUser/', include(MyUsers)),
    path('legal-documents/', include(LGDocs)),
]