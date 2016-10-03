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
        return render(request, 'packages/create_packages.html')
    else:
        form = PackageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            package = form.save(commit=False)
            package.user = request.user
            package.save()

            return render(request, 'packages/index.html', {'package': package})
        context = {
                "form": form,
         }

        return render(request, 'packages/create_package.html', context)


def delete_package(request, package_id):
    package = Package.objects.get(pk=package_id)
    package.delete()
    packages = Package.objects.filter(user=request.user)
    return render(request, 'package/index.html', {'packages': packages})

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/login_user.html')
    else:
        packs = Package.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            packs = packs.filter(
                Q(reference_number__icontains=query) |
                Q(status__icontains=query)
            ).distinct()
            return render(request, 'packages/index.html', {
                'packages': packs,

            })
        else:
            return render(request, 'packages/index.html', {'packages': packs})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'packages/login_user.html', context)


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
                return render(request, 'packages/login_user.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'packages/login_user.html', {'error_message': 'Invalid login'})
    return render(request, 'packages/login_user.html')


#Direct Warehouse Managers and Drivers here
#Method will return appropriate context + template per user
def update_package_status(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/login_user.html')

    else:
        packages = Package.objects.filter(user=request.user)
        drivers = Driver.objects.all()

        package_instance = Package()
        statuses = package_instance.get_statuses() #In template -> Check If Package is in office. If it is, let user pick In and out of branch and satellite offices

        branch_instance = Branch()
        satellite_offices = branch_instance.get_satellite_offices()
        branch_offices = branch_instance.get_branch_offices()

        if User.objects.get.groups.filter(name="warehouse_manager"): # do something #Don't know if this will work yo
            context = {'packages': packages}

            form = request.POST

            if request.method == 'POST':

                selected_driver_id = get_object_or_404(Driver, pk=request.POST.get('driver_id'))
                package = Package.objects.get(pk=request.POST.get('driver_id'))
                package.entry_set.add(selected_driver_id)


                #Driver.

                #>> > b = Blog.objects.get(id=1)
                #>> > e = Entry.objects.get(id=234)
                #>> > b.entry_set.add(e)  # Associates Entry e with Blog b.

                '''
                AND

                Hack AF

                In template check:

                {% if packages AND statuses AND satellite_offices AND branch offices %}
                Display this shit
                {% else %}
                Display That shit
                {% endif %}
                '''
            return render(request, 'packages/update_packages.html', context) #fix me

        elif User.objects.get.groups.filter(name="client"):
            context = {'packages': packages, 'drivers': drivers, 'statuses': statuses,
                       'satellite_offices': satellite_offices, 'branch_offices': branch_offices}

            return render(request, 'packages/update_packages.html', context) #fix me


def track_packages(request):
    if not request.user.is_authenticated():
        return render(request, 'packages/login_user.html')
    else:
        packages = Package.objects.filter(user=request.user)

    return render(request, 'packages/track_packages.html', {'packages': packages})


def cancel_package(request, package_id):
    undesired_statuses = [
            'Collected',
            'Out For Delivery',
            'Delivered',
            'Failed',
            'Delayed',
            'Misrouted',
            'Lost',
            'Damaged'
    ]
    if Package.get(pk=package_id) not in undesired_statuses:
        package = Package.objects.get(pk=package_id)
        package.status = 'Cancelled'
        packages = Package.objects.filter(user=request.user)
        return render(request, 'packages/index.html', {'packages': packages})

    else:
        return render('packages/index.html', error_message='Error: Packages Cannot Be Cancelled After Collection')


def extra(request, package_id):
    if not request.user.is_authenticated():
        return render(request, 'packages/login_user.html')
    else:
        user = request.user
        package = get_object_or_404(Package, pk=package_id)
        return render(request, 'packages/index.html', {'package': package, 'user': user})
