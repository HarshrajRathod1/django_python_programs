from django.shortcuts import render
from api.models import Employee
from api.seriailizer import EmployeeSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
# Create your views here.

class emp_CreateAPIView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class emp_ListAPIView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer