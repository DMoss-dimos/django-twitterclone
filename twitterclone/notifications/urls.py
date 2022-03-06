
from django.contrib import admin
from django.urls import path, include
from . import views
import random



urlpatterns = [
    path("notifications/<int:users>/", views.notification, name="notification")
]
