from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
# Create your models here.

class StudentManager(models.Manager):
    def get_pass(self):
        qs=Student.objects.all()
        qs1=qs.filter(sub1__gte=40,sub2__gte=40)
        return qs1
    
    def get_fail(self):
        qs=Student.objects.all()
        qs1=qs.filter(Q(sub1__lt=40)|Q(sub2__lt=40))
        return qs1
    

class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    sub1=models.FloatField()
    sub2=models.FloatField()
    objects=StudentManager()

    def get_total(self):
        return self.sub1+self.sub2
    def get_avg(self):
        return (self.sub1+self.sub2)//2
    
    def find_result(self):
        return "PASS" if self.sub1>=40 and self.sub2>=40 else "FAIL"

class EmployeeModel(models.Manager):
    def all(self):
        qs=super().all()
        qs1=qs.filter(eno=1)
        return qs1


class Employee(models.Model):
    eno=models.BigAutoField(primary_key=True)
    ename=models.CharField(max_length=20)
    salary=models.FloatField()
    hra=models.FloatField()


    objects=EmployeeModel()

    def save(self):
        self.hra=self.salary*15/100
        self.full_clean()
        return super().save()
    

    def clean(self):
        super().clean()
        if self.salary<=0:
            raise ValidationError("Salary is grater than equal to zero")
