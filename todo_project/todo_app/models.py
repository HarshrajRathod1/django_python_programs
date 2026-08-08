from django.db import models

# Create your models here.

class Todo(models.Model):
    id=models.BigAutoField(primary_key=True)
    task=models.CharField(max_length=20)