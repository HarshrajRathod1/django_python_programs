from django.shortcuts import render
from .models import UserRegister
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,TemplateView
from .forms import UserRegisterForm
# Create your views here.

class HomeView(TemplateView):
    template_name="home_temp.html"

class UserCreate(CreateView):
    model=UserRegister
    form_class=UserRegisterForm
    success_url="/alluserlist/"

class UserListView(ListView):
    model=UserRegister
    context_object_name="user"

class SingleUserDetailView(DetailView):
    model=UserRegister

class UserUpdateView(UpdateView):
    model=UserRegister
    fields="__all__"
    template_name="user_update_temp.html"
    success_url="/alluserlist/"

class UserDeleteView(DeleteView):
    model=UserRegister
    success_url="/alluserlist/"


