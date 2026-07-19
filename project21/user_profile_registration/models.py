from django.db import models

# Create your models here.

class UserRegister(models.Model):
    user_id=models.BigAutoField(primary_key=True)
    fname=models.CharField(max_length=15)
    lname=models.CharField(max_length=15)
    uname=models.CharField(max_length=20,unique=True)
    email=models.CharField(max_length=25)
    gender=models.CharField(max_length=7)
    role=models.CharField(max_length=15)
    dob=models.DateField()
    city=models.CharField(max_length=15)
    number=models.IntegerField()

    class Meta:
        db_table="user"

