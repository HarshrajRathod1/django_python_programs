from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from app.models import Product
# Create your views here.

class CreateProduct(CreateView):
    model=Product
    fields=['pname','qty','price']
    success_url='/create_prod/'
    template_name="product_temp.html"