
from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import home

'''
urlpatterns = [
    path('admin/', admin.site.urls),
]
'''

"""

# I add a url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
]


"""

# I add a app url here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('student/', include('student.urls')),
    path('details/', views.details),
]
