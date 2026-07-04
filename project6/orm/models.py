from django.db import models

# Create your models here.
class Student(models.Model):
    rolno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)

class Marks(models.Model):
    rolno=models.IntegerField()
    sub1=models.FloatField()
    sub2=models.FloatField()
    class Meta:
        db_table="marks"

class Books(models.Model):
    bookid=models.IntegerField(primary_key=True)
    bname=models.CharField(max_length=20)
    class Meta:
        db_table="books"

class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    job=models.CharField(max_length=15)
    sal=models.FloatField()
    class Meta:
        db_table="emp"
