from django.contrib import admin
from .models import Cupons, Info_Payment_for_one

# Register your models here.

admin.site.register((Cupons, Info_Payment_for_one))