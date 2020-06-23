from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('shop/',views.Shops.as_view()),
    path('shop/<pk>/',views.ShopsDetail.as_view()),
    path('ratings/',views.Ratings.as_view()),
    path('ratings/<pk>/',views.RatingsDetail.as_view()),
    path('packages/',views.Packages.as_view()),
    path('package/<pk>/',views.PackageDetail.as_view),
]