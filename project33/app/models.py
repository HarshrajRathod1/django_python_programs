from django.db import models

# Create your models here.

class Employess(models.Model):
    eid=models.BigAutoField(primary_key=True)
    ename=models.CharField(max_length=20)
    sal=models.FloatField()
    job=models.CharField(max_length=20,null=True,blank=True)