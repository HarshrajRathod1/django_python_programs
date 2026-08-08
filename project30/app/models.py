from django.db import models

# Create your models here.
class Contacts(models.Model):
    address=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()

class Person(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    contact=models.OneToOneField(Contacts, on_delete=models.CASCADE)
