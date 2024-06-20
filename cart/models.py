from django.db import models
from products.models import AllProducts
from django .contrib.auth.models import User

# Create your models here.

class Cart(models.Model):

    item = models.ForeignKey(AllProducts, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    size = models.CharField(max_length=50, default="None")
    price = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_key = models.CharField(max_length=40, null=True, default='sessionidHere')
    product_id_cart = models.CharField(max_length=10, default='NONE')

    

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Cart"

    def __str__(self):
        return self.item.product_name