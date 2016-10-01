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



def index(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/login.html')
    else:
        packs = Package.objects.filter(user=request.user)
        #more models to be added here
        query = request.GET.get("q")
        if query:
            packs = packs.filter(
                Q(reference_number__icontains=query) |
                Q(status__icontains=query) |
                Q(volumetric_weight__icontains=query) |
                Q(client_address__icontains=query) |
                Q(client_city__icontains=query) |
                Q(driver__icontains=query) |
                Q(receiver_address__icontains=query)

            ).distinct

            return render(request, 'packages/index.html',)
        else:
            return render(request, 'packages/index.html', {'packs': packs})



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'packages/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                packs = Package.objects.filter(user=request.user)
                return render(request, 'packages/index.html', {'packs': packs})
            else:
                return render(request, 'packages/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'packages/login.html', {'error_message': 'Invalid login'})
    return render(request, 'packages/login.html')
