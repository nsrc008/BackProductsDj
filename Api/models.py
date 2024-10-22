from django.db import models

class Products(models.Model):
    productName = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
