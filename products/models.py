from django.contrib.auth.models import User
from django.db import models
from utilities.utilities import *
from django.utils.timezone import now

# Create your models here.


class Flavour(models.Model):
    flavour_name = models.CharField(max_length=255)
    flavour_slug = models.SlugField(max_length=255)
    flavour_filter_color = models.CharField(max_length=100, null=True, default="none")

    def __str__(self):
        return self.flavour_name

    class Meta:
        verbose_name = ("AllFlavours")
        verbose_name_plural = "Flavours"


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("AllCategory")
        verbose_name_plural = "Category"
    


class AllProducts(models.Model):
    products_id = models.CharField(max_length=10, unique=True)
    product_sno = models.AutoField(primary_key=True, unique=True)
    product_slug = models.SlugField(max_length=255)
    product_image = models.ImageField(upload_to='Sell/')
    product_name = models.CharField(max_length=50)
    product_manufacturer = models.CharField(max_length=50, default='Unknown')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    product_price = models.CharField(max_length=8, null=False, default='0.00')
    product_dateAdded = models.DateField(auto_now=False, default=now)
    product_TimeAdded = models.TimeField(default=now)
    product_desc_sm = models.CharField(max_length=300, null=True, default='No Discription from Seller')
    product_desc_lg = models.TextField(null=True, default='No Discription from Seller')
    product_seller = models.CharField(max_length=20)
    product_rating = models.IntegerField(null=True, default="0") # type: ignore
    product_origin = models.CharField(max_length=10)
    product_totalOrders = models.IntegerField(null=True, default="0") # type: ignore

    

    class Meta:
        verbose_name = ("AllProduct")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.product_name + " price is " + self.product_price


class ProductComment(models.Model):
    sno = models.AutoField(primary_key=True)
    Productcomment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Productpost = models.ForeignKey(AllProducts, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    Productcomment_date_stamp = models.DateField(auto_now=False, default=now)
    Productcomment_time_stamp = models.TimeField(default=now)
    Productcomment_datetime_stamp = models.DateTimeField(default=now)
    Likes = models.IntegerField(default=0)
    disLike = models.IntegerField(default=0)

    def __str__(self):
        return self.Productcomment[0:15] + '...         by "' + self.user.username + '"'


class CommentLike(models.Model):
    sno = models.AutoField(primary_key=True, unique=True)
    commentIs = models.ForeignKey(ProductComment, on_delete=models.CASCADE)
    useris = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.BooleanField(null=True)
    icon = models.CharField(max_length=200, null=False, default='<i class="bi bi-hand-thumbs-up"></i>')

    class Meta:
        verbose_name = ("Like Record")
        verbose_name_plural = ("Like Record")

    def __str__(self):
        return self.commentIs.Productcomment[0:15] + '... has liked by"' + self.useris.username


class CommentDislike(models.Model):
    sno = models.AutoField(primary_key=True, unique=True)
    commentIs = models.ForeignKey(ProductComment, on_delete=models.CASCADE)
    useris = models.ForeignKey(User, on_delete=models.CASCADE)
    disliked = models.BooleanField(null=True)
    icon = models.CharField(max_length=200, null=False, default='<i class="bi bi-hand-thumbs-down"></i>')

    class Meta:
        verbose_name = ("Dislike Record")
        verbose_name_plural = ("Dislike Record")

    def __str__(self):
        return self.commentIs.Productcomment[0:15] + '... has Disliked by"' + self.useris.username