from django.shortcuts import render
from todo_app.models import Todo
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_view(request):
    form=UserCreationForm()
    return render(request,"register.html",context={'form':form})



