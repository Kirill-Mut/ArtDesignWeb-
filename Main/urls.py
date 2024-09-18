from django.urls import path, include
from Main import views
from . import views
from .views import base, registration_view, login_view, registration_login_view, application_view, house_list, house_detail, house_create, house_update, house_delete, projects, contacts, about_us
from .views import contacts_create, contacts_delete, contacts_list, contacts_update














urlpatterns = [
    path("", views.base, name="base"),
    path('9de4a97425678c5b1288aa70c1669a64/', registration_view, name='register'),
    path('d56b699830e77ba53855679cb1d252da/', login_view, name='login'),
    path('b9ac4bddb2e16da5985ee1be924858ba/', registration_login_view, name='register_login'),
    path('apply/', application_view, name='application'),
    path('house/', house_list, name='house_list'),
    path('house/<int:pk>/', house_detail, name='house_detail'),
    path('house/new/', house_create, name='house_create'),
    path('house/<int:pk>/edit/', house_update, name='house_update'),
    path('house/<int:pk>/delete/', house_delete, name='house_delete'),
    path('contacts/', contacts_list, name='contacts_list'),
    path('contacts/new/', contacts_create, name='contacts_create'),
    path('contacts/<int:pk>/edit/', contacts_update, name='contacts_update'),
    path('contacts/<int:pk>/delete/', contacts_delete, name='contacts_delete'),
    path('contactss/', contacts, name='contacts'),
    path('projects/', projects, name='projects'),
    path('about_us/', about_us, name='about_us'),
    

]