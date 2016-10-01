from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.surname


class Branch(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " - " + self.city


class Package(models.Model):
    reference_number = models.CharField(max_length=10)
    receiver_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    volumetric_weight = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=50)
    id_required = models.BooleanField(default=True)
    client = models.ForeignKey(Client, default=1)

    def __str__(self):
        return "Package " + self.reference_number


class WarehouseManager(models.Model):
    branch = models.OneToOneField(Branch, default=1)


class Driver(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    warehouse_manager = models.ForeignKey(WarehouseManager, default=1)

    def __str__(self):
        return self.name + " " + self.surname




