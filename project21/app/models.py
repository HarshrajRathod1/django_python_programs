from django.db import models

# Create your models here.

class Customer(models.Model):
    cust_id=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone_number=models.IntegerField()
    date_of_birth=models.DateField()
    class Meta:
        db_table="cust"
