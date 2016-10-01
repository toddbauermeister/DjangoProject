from django.db import models
from django.utils import timezone


class Branch(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def get_branch_offices(self):

        satellite_offices = [
            'Swellendam',
            'Observatory',
            'Kloof',
            'Hillcrest'
            'Hatfield',
            'Sunnyside',
            'Parktown',
            'Sandton'
        ]

        return satellite_offices

    def get_satellite_offices(self):

        satellite_offices = [
            'Cape Town',
            'Durban',
            'Pretoria',
            'Johannesburg'
        ]

        return satellite_offices



    def __str__(self):
        return self.name + " - " + self.city


class Package(models.Model):
    reference_number = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    volumetric_weight = models.DecimalField(max_digits=10, decimal_places=2)
    client_address = models.CharField(max_length=50)
    client_city = models.CharField(max_length=50)
    receiver_address = models.CharField(max_length=50)
    receiver_city = models.CharField(max_length=50)
    id_required = models.BooleanField(default=True)
    user = models.ForeignKey(User, default=1)
    branch = models.ForeignKey(Branch, default=1)

    def get_statuses(self):
        statuses = [
            'Cancelled',
            'Collected',
            'Out For Delivery',
            'Delivered',
            'Failed',
            'Delayed',
            'Misrouted',
            'Lost',
            'Damaged'
        ]

        return statuses

    def __str__(self):
        return "Package " + self.reference_number


class Driver(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.surname




