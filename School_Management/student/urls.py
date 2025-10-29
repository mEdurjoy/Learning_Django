
from django.urls import path
from . import views
#from .views import home

'''
urlpatterns = [
    path('admin/', admin.site.urls),
]
'''
# I add a url
urlpatterns = [
    path('profile/', views.profile),
]
