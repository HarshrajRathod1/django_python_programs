from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    name=models.CharField(max_length=20) 
    uname=models.CharField(max_length=20,primary_key=True) 
    password=models.CharField(max_length=15)

    class Meta:
        db_table="register"

class Employee(models.Model):
    empno=models.IntegerField(primary_key=True) 
    ename=models.CharField(max_length=20) 
    job=models.CharField(max_length=15) 
    sal=models.FloatField()

    class Meta:
        db_table="emp"