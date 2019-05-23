from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120, null=False,default="")
    description = models.TextField(null=False,default="")
    price = models.DecimalField(null=False,default=0,decimal_places=2,max_digits=1000)
    summary = models.TextField(default="This is cool",null=False,blank=True)
    featured = models.BooleanField(default=True)