from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request):
    return HttpResponse("This is the student profile page.")

def details(request):
    return render(request, 'student/index.html')