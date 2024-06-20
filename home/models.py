from django.db import models


class Contact(models.Model):

    ContactUser = models.CharField(max_length=100)
    ContactPhone = models.CharField(max_length=13)
    ContactEmail = models.CharField(max_length=150)
    ContactMessage = models.TextField()

    

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.ContactUser + " Contacted you."