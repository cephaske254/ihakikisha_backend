from django.urls import path, include
from . import views

urlpatterns = [
    path('shops/',views.Shops.as_view()),
    path('shops/<pk>/',views.ShopsDetail.as_view()),
    
    path('ratings/',views.Ratings.as_view()),
    path('ratings/<pk>/',views.RatingsDetail.as_view()),

    path('packages/',views.Packages.as_view()),
    path('packages/<pk>/',views.PackageDetail.as_view()),

    path('product-set/',views.ProductSets.as_view(),name='add_set'),
    path('product-set/<pk>/',views.ProductSetDetails.as_view(),name='update_set'),

    path('products/',views.Products.as_view(),name='add_product'),
    path('products/<pk>/',views.ProductDetails.as_view(),name='get_product'),

    path('distributors/', views.DistributorProfile.as_view()),
    path('distributors/<pk>/', views.DistributorProfileDetail.as_view()),

    path('farmers/', views.FarmerProfile.as_view()),
    path('farmers/<pk>/', views.FarmerProfileDetail.as_view()),

    path('manufacturers/', views.ManufacturerProfile.as_view()),
    path('manufacturers/<pk>/', views.ManufacturerProfileDetail.as_view()),
    
    path('retrieve/<uuid>/', views.RetrieveProduct.as_view()),
]
