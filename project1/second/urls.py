from django.contrib import admin
from django.urls import path
from second.views import second
from second.views import third
urlpatterns = [
    path('second/',second),
    path('third/',third),
]

