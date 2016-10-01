from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import PackageForm, UserForm
from .models import User, Branch, Package, WarehouseManager, Driver



def mypacks(request):
    return HttpResponse("Hello, world. You're at the package index.")

def create_package(request):
    if not request.client.is_authenticated():
        return render(request, 'packages/login.html')
    else:
        form = PackageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            package = form.save(commit=False)
            package.user = request.client



