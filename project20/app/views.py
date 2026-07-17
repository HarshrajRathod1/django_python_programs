from django.shortcuts import render
from django.views.generic import DetailView
from app.models import Employee


# Create your views here.

class EmpDetailView(DetailView):
    model=Employee
    

