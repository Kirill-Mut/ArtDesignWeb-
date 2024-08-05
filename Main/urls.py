from django.urls import path, include
from Main import views
from . import views
from .views import base















urlpatterns = [
    path("", views.base, name="base"),
    

]