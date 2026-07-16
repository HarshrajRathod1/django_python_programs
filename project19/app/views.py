from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from app.models import Product
from app.forms import ProductForm
# Create your views here.

class CreateProduct(CreateView):
    model=Product
    form_class=ProductForm
    success_url='/create_prod/'
    template_name="product_temp.html"

class ListProduct(ListView):
    model=Product
    template_name="all_product_temp.html"
    context_object_name="prod"