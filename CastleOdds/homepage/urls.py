from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('sports/', views.sports, name='sports'),
]