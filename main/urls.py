from django.urls import path, include
from . import views

urlpatterns = [
    path('distributors/', views.DistributorProfile.as_view()),
    path('distributors/<pk>', views.DistributorProfileDetail.as_view()),
    path('farmers/', views.FarmerProfile.as_view()),
    path('farmers/<pk>', views.FarmerProfileDetail.as_view()),
    path('manufacturers/', views.ManufacturerProfile.as_view()),
    path('manufacturers/<pk>', views.ManufacturerProfileDetail.as_view()),
]