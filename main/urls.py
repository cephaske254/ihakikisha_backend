from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('add-shop/',views.ShopProfile.as_view()),
    path('add-shop/<pk>/'views.ShopProfileDetail.as_view()),
    path('add-ratings/'views.RatingsProfile.as_view()),
    path('add-ratings/<pk>/'views.RatingsProfileDetail.as_view()),
    path('add-package/',views.PackageProfile.as_view()),
    path('add-package/<pk>/'views.PackageProfileDetail.as_view),
]