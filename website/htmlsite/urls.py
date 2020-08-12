from django.contrib import admin
from django.urls import path, include, re_path
from .views import page

urlpatterns = [
    path('test/', page),
    re_path(r'^', page)
]
