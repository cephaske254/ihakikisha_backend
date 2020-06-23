from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('shop/',views.ShopProfile.as_view()),
    path('shop/<pk>/',views.ShopProfileDetail.as_view()),
    path('ratings/',views.RatingsProfile.as_view()),
    path('ratings/<pk>/',views.RatingsProfileDetail.as_view()),
    path('package/',views.PackageProfile.as_view()),
    path('package/<pk>/',views.PackageProfileDetail.as_view),
]