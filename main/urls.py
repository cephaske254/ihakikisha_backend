from django.urls import path, include
from . import views

urlpatterns = [
    path('distributors/', views.DistributorProfile.as_view()),
    path('distributors/<pk>', views.DistributorProfileDetail.as_view()),
    path('farmers/', views.FarmerProfile.as_view()),
    path('farmers/<pk>', views.FarmerProfileDetail.as_view()),
    path('manufacturers/', views.ManufacturerProfile.as_view()),
    path('manufacturers/<pk>', views.ManufacturerProfileDetail.as_view()),
    path('shop/',views.ShopProfile.as_view()),
    path('shop/<pk>/',views.ShopProfileDetail.as_view()),
    path('ratings/',views.RatingsProfile.as_view()),
    path('ratings/<pk>/',views.RatingsProfileDetail.as_view()),
    path('package/',views.PackageProfile.as_view()),
    path('package/<pk>/',views.PackageProfileDetail.as_view),
]