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

class ListProduct1(ListView):
    model=Product
    template_name="all_product_temp.html"
    context_object_name="prod"

    def get_queryset(self):
        qs= super().get_queryset()
        qs=qs.filter(price__gte=5000)
        return qs
    
class ListProduct2(ListView):
    model=Product
    template_name="all_product_temp.html"
    context_object_name="prod"

    def get(self,request):
        self.p=int(request.GET.get("price"))
        return super().get(self.p)
    
    def get_queryset(self):
        qs= super().get_queryset()
        qs=qs.filter(price__gte=self.p)
        return qs
