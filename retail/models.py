from django.db import models
from django.contrib.auth.models import User

from products.models import AllProducts

# Create your models here.


class Cupons(models.Model):

    # Capitalized one is the value means "Used"(1) is the value of "used"(2)
    UseCHOICES = (('used', 'used'),('unused', 'unused'))

    cupon_sno = models.AutoField(primary_key=True)
    cupon_id = models.CharField(max_length=20)
    cupon_name = models.CharField(max_length=50)
    cupon_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cupon_discount = models.IntegerField()
    cupon_alloted_day = models.DateField(auto_now=True)
    cupon_expiry_day = models.DateField(auto_now=False, null=True)
    cupon_code = models.CharField(max_length=10)
    cupon_used_status = models.CharField(max_length=50, choices=UseCHOICES, default='unused')

    class Meta:
        verbose_name_plural = ("cupons")

    def __str__(self):
        return self.cupon_name + "  belongs to  " + self.cupon_user.first_name

class Info_Payment_for_one(models.Model):
    order_sno = models.AutoField(primary_key=True)
    user_is_orderd = models.BooleanField(null=True)
    user_order_id = models.CharField(max_length=10, null=True)
    user_order_Code = models.CharField(max_length=13)
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    user_order_nameFirst = models.CharField(max_length=50)
    user_order_nameLast = models.CharField(max_length=50)
    user_order_email = models.CharField(max_length=150)
    user_order_address1 = models.CharField(max_length=500)
    user_order_address2_opt = models.CharField(max_length=500,null=True)
    user_order_country = models.CharField(max_length=50)
    user_order_state = models.CharField(max_length=50)
    user_order_pin = models.CharField(max_length=6)
    user_order_phone1 = models.CharField(max_length=13)
    user_order_phone2_opt = models.CharField(max_length=13, null=True)
    user_order_cupon_applied = models.BooleanField()
    user_order_cupon = models.ForeignKey(Cupons, on_delete=models.CASCADE, null=True) 
    user_order_product = models.ForeignKey(AllProducts, on_delete=models.CASCADE) 
    user_order_product_qty = models.IntegerField()
    user_order_product_size = models.CharField(max_length=50)


    class Meta:
        verbose_name = "Info_Payment_for_one"
        verbose_name_plural = "Info_Payment_for_one"

    def __str__(self):
        return self.customer.username + " orderd Something With the name of " + self.user_order_nameFirst + " " + self.user_order_nameLast
