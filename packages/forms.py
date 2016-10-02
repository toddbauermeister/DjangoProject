from django import forms
from django.contrib.auth.models import User

from .models import User, Branch, Package, Driver


class PackageForm(forms.ModelForm):

    class Meta:
        model = Package
        fields = ['reference_number', 'volumetric_weight', 'status', 'client_address',
                  'client_city', 'receiver_address', 'receiver_city']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class DriverSelectForm(forms.ModelForm):
    drivers = forms.ModelChoiceField(queryset=Driver.objects.all())

