from django.shortcuts import render
from app.models import Customer
from app.forms import CustomerForm
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
# Create your views here.

class HomeView(TemplateView):
    template_name="app_base.html"

class CustCreateView(CreateView):
    model=Customer
    form_class=CustomerForm
    template_name="app_create_temp.html"
    success_url="/app_home"

class CustListView(ListView):
    model=Customer
    template_name="app_allcust_temp.html"
    context_object_name="customer"

class CustUpdateView(UpdateView):
    model=Customer
    form_class=CustomerForm
    template_name="app_create_temp.html"
    success_url="/cust_all"

class CustDeleteView(DeleteView):
    model=Customer
    template_name="app_delete_temp.html"
    success_url="/cust_all"

