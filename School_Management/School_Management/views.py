from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Welcome to the School Management System Home Page!")   


def details(request):
    return render(request, 'student/index.html')