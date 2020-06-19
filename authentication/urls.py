
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('token/',views.CustomAuthToken.as_view())
]
