from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    supplier_price = models.FloatField()
    selling_price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # how to represent the object in the database
    def __str__(self):
        return self.name