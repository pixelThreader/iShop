from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdditionalUserCredentials(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # My Custom Modles

    GENDER_CHOICE = [('Male', 'Male'),('Female', 'Female')]

    Emergency_id01 = models.CharField(max_length=10, unique = True)
    Emergency_id02 = models.CharField(max_length=10, unique = True)
    phone = models.CharField(max_length=13)
    phone_alt = models.CharField(max_length=13, default=None, null=True)
    gender = models.CharField(max_length=6, choices= GENDER_CHOICE)
    birth = models.DateField(auto_now=False)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pinCode = models.CharField(max_length=6)
    Avatar = models.ImageField(upload_to="Uploads_from_User/profile/avatar", default="Uploads_from_User/profile/avatar/person-circle.svg")

    class Meta:
        verbose_name = "UserCredentials"
        verbose_name_plural = "AdditionalUserCredentials"

    def __str__(self):
        return self.user.username
