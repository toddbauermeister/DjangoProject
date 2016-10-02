from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import PackageForm, UserForm
from .models import User, Branch, Package, Driver


def create_package(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/create_package.html')
    else:
        form = PackageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            package = form.save(commit=False)
            package.user = request.client

            return render(request, 'packages/extra.html', {'package': package})
        context = {
                "form": form,
         }
        return render(request, 'packages/create_package.html', context)


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/login.html')
    else:
        packs = Package.objects.filter(user=request.user)
        #more models to be added here

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


#Direct Warehouse Managers and Drivers here
#Method will return appropriate context + template per user
def update_package_status(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/updatepackages.html')

    else:
        packages = Package.objects.filter(user=request.user)
        drivers = Driver.objects.all()
        statuses = Package.get_statuses() #In template -> Check If Package is in office. If it is, let user pick In and out of branch and satellite offices
        satellite_offices = Branch.get_satellite_offices()
        branch_offices = Branch.get_branch_offices()

        if request.user.get_username != 'warehousemanager':
            context = {'packages': packages, 'drivers': drivers, 'statuses': statuses,
                   'satellite_offices': satellite_offices, 'branch_offices': branch_offices }

            return render(request, 'packages/whmngr_update_package', context)

        else:
           context = {'packages': packages, 'statuses': statuses,
                  'satellite_offices': satellite_offices, 'branch_offices': branch_offices }

           return render(request, 'packages/driver_update_package', context)


def track_packages(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/login.html')
    else:
        packages = Package.objects.filter(user=request.user)

    return render(request, 'packages/track_packages.html', {'packages': packages})


def cancel_package(request, package_id):
    package = Package.objects.get(pk=package_id)
    package.delete()
    package = Package.objects.filter(user=request.user)
    return render(request, 'lms/index.html', {'books': package})


def extra(request, package_id):
    if not request.user.is_authenticated():
        return render(request, 'packages/login.html')
    else:
        user = request.user
        package = get_object_or_404(Package, pk=package_id)
        return render(request, 'packages/extra.html', {'package': package, 'user': user})