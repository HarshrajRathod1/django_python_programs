"""
URL configuration for project6 project.

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
from django.urls import path
from orm.views import home,insert_book
from orm.views import homeFind,showresult
from orm.views import findresultall
from orm.views import findjobhome,findjob
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",home),
    path("insert_book/",insert_book),
    path("home_find/",homeFind),
    path("Find_marks/",showresult),
    path('findresultall/',findresultall),
    path('findjobhome/',findjobhome),
    path('findjob/',findjob)
]
