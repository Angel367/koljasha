from django.contrib import admin
from django.urls import path, include, re_path
from .views import main_page, main_redirect

urlpatterns = [
    path('main/', main_page),
    re_path(r'^', main_redirect)
]
