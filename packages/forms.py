from django import forms
from django.contrib.auth.models import User

from .models import  User, Branch, Package, Driver


class PackageForm(forms.ModelForm):

    class Meta:
        model = Package
        fields = ['', 'book_title', 'book_genre', 'book_cover']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
