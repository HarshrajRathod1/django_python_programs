"""
URL configuration for project27 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,reverse_lazy
from app.views import *
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_register),
    path('login/',loginview,name="login"),
    path('dashboard/',dashboardview),
    path('logout/',loginview),
    #function based view for change password
    path('password_change/',passwordchange_view),

    #class based view for changing password
    path(
        'password_change1/',
            PasswordChangeView.as_view(
                template_name="password_change_temp.html",
                success_url=reverse_lazy("login"),
            )
        ),
]
