from django.urls import path, include
from . import views

urlpatterns = [
    path('product-set/',views.ProductSet.as_view()),
    path('product-set/<pk>/',views.ProductSetDetails.as_view()),
    path('products/',views.Products.as_view()),
    path('products/<pk>/',views.ProductDetails.as_view()),
    path('distributors/', views.DistributorProfile.as_view()),
    path('distributors/<pk>', views.DistributorProfileDetail.as_view()),
    path('farmers/', views.FarmerProfile.as_view()),
    path('farmers/<pk>', views.FarmerProfileDetail.as_view()),
    path('manufacturers/', views.ManufacturerProfile.as_view()),
    path('manufacturers/<pk>', views.ManufacturerProfileDetail.as_view()),
    path('shops/',views.Shops.as_view()),
    path('shops/<pk>/',views.ShopDetail.as_view()),
    path('ratings/',views.Ratings.as_view()),
    path('ratings/<pk>/',views.RatingsDetail.as_view()),
    path('packages/',views.Packages.as_view()),
    path('packages/<pk>/',views.PackageDetail.as_view()),
]

