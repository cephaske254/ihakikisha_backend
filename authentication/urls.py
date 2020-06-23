from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('register/',views.Register.as_view()),
    path('token/',views.CustomAuthToken.as_view()),
]