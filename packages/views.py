from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def mypacks(request):
    return render(request, 'base_template.html')

