from django.contrib import admin
from django.urls import path, include, re_path
from .views import main_page
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('main/', main_page),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
