from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('users/<pk>/', views.UserDetail.as_view()),
    path('register/',views.Register.as_view()),
    path('token/',views.CustomAuthToken.as_view()),
]
