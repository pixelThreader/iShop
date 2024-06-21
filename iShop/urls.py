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