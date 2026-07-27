from django.db import models

# Create your models here.

class User(models.Model):
    user=models.CharField(max_length=20,primary_key=True)
    pwd=models.CharField(max_length=15)

class Emails(models.Model):
   user=models.CharField(max_length=20)
   subject=models.CharField(max_length=20)
   content=models.CharField(max_length=100)
    
