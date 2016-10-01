from django import forms
from django.contrib.auth.models import Client
from .models Client, Branch, Package, WarehouseManager, Driver


class PackageForm(forms.ModelForm):

    class Meta:
        model = Package
        fields = ['', 'book_title', 'book_genre', 'book_cover']


class ClientForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['username', 'email', 'password']
