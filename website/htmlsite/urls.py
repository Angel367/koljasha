from django.contrib import admin
from django.urls import path, include, re_path
from .views import main_page, ssl_func
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('main/', main_page),
    path('.well-known/acme-challenge/NHts6AuYz8wvCGH-ijNDeRXSbPMMgVbG7roo4IBaUYo', ssl_func),
    path('.well-known/acme-challenge/NHts6AuYz8wvCGH-ijNDeRXSbPMMgVbG7roo4IBaUYo/', ssl_func),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
