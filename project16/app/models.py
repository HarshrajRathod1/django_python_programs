from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    sub1=models.FloatField()
    sub2=models.FloatField()

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
