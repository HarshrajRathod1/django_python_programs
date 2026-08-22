"""
URL configuration for webapi8 project.

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
from api.views import emp_CreateAPIView
from api.views import emp_ListAPIView
from api.views import emp_RetrieveAPIView
from api.views import emp_UpdateAPIView
from api.views import emp_DestroyAPIView

from api.views import emp_ListCreateAPIView
from api.views import emp_ReteriveUpdateAPIView
from api.views import emp_ReterieveDestroyAPIView
from api.views import emp_RetrieveUpdateDestoryAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('empcreate/',emp_CreateAPIView.as_view()),
    path('emplist/',emp_ListAPIView.as_view()),
    path('empget/<int:pk>/',emp_RetrieveAPIView.as_view()),
    path('empupdate/<int:pk>/',emp_UpdateAPIView.as_view()),
    path('empdelete/<int:pk>/',emp_DestroyAPIView.as_view()),

    path('emplistcreate/',emp_ListCreateAPIView.as_view()),
    path('empgetupdate/<int:pk>/',emp_ReteriveUpdateAPIView.as_view()),
    path('empgetdelete/<int:pk>/',emp_ReterieveDestroyAPIView.as_view()),
    path('empgetupdatedelete/<int:pk>/',emp_RetrieveUpdateDestoryAPIView.as_view()),
]
