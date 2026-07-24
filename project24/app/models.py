from django.db import models

# Create your models here.

class Users(models.Model):
    uname=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)

    class Meta:
        db_table="users"

class Emails(models.Model):
    uname=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    email=models.CharField(max_length=100)

    class Meta:
        db_table="emails"