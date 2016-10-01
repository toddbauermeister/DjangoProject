from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from models import Package
from models import Driver
from models import Branch


def update_package_status(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/login.html')

    else:
        packages = Package.objects.filter(user=request.user)
        drivers = Driver.objects.all()
        statuses = Package.get_statuses() #In template -> Check If Package is in office. If it is, let user pick In and out of branch and satellite offices
        satellite_offices = Branch.get_satellite_offices()
        branch_offices = Branch.get_branch_offices()

        context = {'packages': packages, 'statuses': statuses, 'satellite_offices': satellite_offices}

        return request, 'packages/update_package', context






























































