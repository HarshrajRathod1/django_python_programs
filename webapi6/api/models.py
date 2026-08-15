from django.db import models

# Create your models here.

class Student(models.Model):
    rno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=15)


