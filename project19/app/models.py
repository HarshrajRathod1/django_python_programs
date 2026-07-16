from django.db import models

# Create your models here.

class Product(models.Model):
    prodID=models.BigAutoField(primary_key=True)
    pname=models.CharField(max_length=20)
    qty=models.IntegerField()
    price=models.FloatField()