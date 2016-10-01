from django.http import HttpResponse


def mypacks(request):
    return HttpResponse("Hello, world. You're at the package index.")