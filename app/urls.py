from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('app/', views.testapp, name="testapp"), 
]
