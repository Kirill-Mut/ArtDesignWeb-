from django.urls import path, include
from Main import views
from . import views
from .views import base, registration_view, login_view, registration_login_view, application_view















urlpatterns = [
    path("", views.base, name="base"),
    path('9de4a97425678c5b1288aa70c1669a64/', registration_view, name='register'),
    path('d56b699830e77ba53855679cb1d252da/', login_view, name='login'),
    path('b9ac4bddb2e16da5985ee1be924858ba/', registration_login_view, name='register_login'),
    path('apply/', application_view, name='application'),
    

]