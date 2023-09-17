from django.db import models

# Create your models here.

class destination(models.Model):
    StudentName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Date = models. DateTimeField(auto_now=False, auto_now_add=False)
