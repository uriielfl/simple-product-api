from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__ (self):
        return str(self.id)

class ProductImages(models.Model):
    productId = models.ForeignKey(Products, related_name="productId", on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    image_created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.productId)