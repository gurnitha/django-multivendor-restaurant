# config/settings.py

# Django modules
from django.contrib import admin
from django.urls import path

# Locals
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
