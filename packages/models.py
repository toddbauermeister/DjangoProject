from django.db import models
from django.utils import timezone

# Create your models here.

class Packages(models.Model):
    location= models.CharField(max_length=30)
