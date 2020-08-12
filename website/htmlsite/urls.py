from django.contrib import admin
from django.urls import path, include
from .views import page

urlpatterns = [
    path('test/', page),
]

