from django.db import models

# Create your models here.

class Employee(models.Model):
    empno=models.BigAutoField(primary_key=True)
    ename=models.CharField(max_length=20)
    job=models.CharField(max_length=20)
    sal=models.FloatField()

