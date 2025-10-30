from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request):
    return HttpResponse("This is the student profile page.")

def details(request):
    user_info = {
        'name': 'John Doe',
        'age': 20,
        'major': 'Computer Science'
    }
    return render(request, 'student/index.html',user_info)