from django.shortcuts import render
from api.models import Employee
from api.seriailizer import EmployeeSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.

# Only Create
class emp_CreateAPIView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# List all The Emlpoyess
class emp_ListAPIView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# Get single Employee with pk path parameter
class emp_RetrieveAPIView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# Update single Employee with pk path parameter
class emp_UpdateAPIView(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# Delete Single Employee with pk path parameter
class emp_DestroyAPIView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# List all Employess and Create new Employee 
class emp_ListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# Get single Employee and update Employee with pk path parameter
class emp_ReteriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# Get Single Employee and Delete Employee with pk path parameter
class emp_ReterieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class emp_RetrieveUpdateDestoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer