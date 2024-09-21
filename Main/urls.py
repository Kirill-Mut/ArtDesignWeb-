from django.urls import path, include
from Main import views
from . import views
from .views import base, registration_login_view, application_view, house_list, house_detail, house_create, house_edit, house_delete, projects, contacts, about_us
from .views import contacts_create, contacts_delete, contacts_list, contacts_update














urlpatterns = [
    path("", views.base, name="base"),
    path('authorization/', registration_login_view, name='register_login'),
    path('apply/', application_view, name='application'),
    path('house/', house_list, name='house_list'),
    path('house/<int:house_id>/', house_detail, name='house_detail'),
    path('house/new/', house_create, name='house_create'),
    path('house/<int:house_id>/edit/', house_edit, name='house_edit'),
    path('house/<int:pk>/delete/', house_delete, name='house_delete'),
    path('contacts/', contacts_list, name='contacts_list'),
    path('contacts/new/', contacts_create, name='contacts_create'),
    path('contacts/<int:pk>/edit/', contacts_update, name='contacts_update'),
    path('contacts/<int:pk>/delete/', contacts_delete, name='contacts_delete'),
    path('contactss/', contacts, name='contacts'),
    path('projects/', projects, name='projects'),
    path('about_us/', about_us, name='about_us'),
    

]