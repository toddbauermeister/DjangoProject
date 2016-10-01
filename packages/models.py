from django.db import models
from django.utils import timezone

# Create your models here.


class Package(models.Model):
    reference_number = models.CharField(max_length=10)
    receiver_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    volumetric_weight = models.DecimalField(max_digits=10,decimal_places=2)
    destination = models.CharField(max_length=50)
    id_required = models.BooleanField(default=True)
    client = models.ForeignKey(Client, default=1)


class WarehouseManager():
    branch = models.OneToOneField(Branch, default=1)


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Driver(models.Model):
    name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    warehouse_manager = models.ForeignKey(WarehouseManager, default=1)


class Branch():
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)



