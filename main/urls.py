from django.urls import path, include
from . import views

urlpatterns = [
    path('shops/',views.Shops.as_view()),
    path('shops/<pk>/',views.ShopsDetail.as_view()),

    path('packages/',views.Packages.as_view()),
    path('packages/<pk>/',views.PackageDetail.as_view()),

    path('product-set/',views.ProductSets.as_view(),name='add_set'),
    path('product-set/<pk>/',views.ProductSetDetails.as_view(),name='update_set'),

    path('products/bulk/', views.CreateBulkProducts.as_view()),
    path('products/',views.Products.as_view(),name='add_product'),
    path('products/<pk>/',views.ProductDetails.as_view(),name='get_product'),

    path('distributors/', views.DistributorProfile.as_view()),
    path('distributors/<pk>/', views.DistributorProfileDetail.as_view()),

    path('farmers/', views.FarmerProfile.as_view()),
    path('farmers/<pk>/', views.FarmerProfileDetail.as_view()),

    path('manufacturers/', views.ManufacturerProfile.as_view()),
    path('manufacturers/<pk>/', views.ManufacturerProfileDetail.as_view()),
    
    path('retrieve/<uuid>/', views.RetrieveProduct.as_view()),

    path('my-profile/', views.Profile.as_view()),
    path('my-product-sets/', views.MyProductsets.as_view()),
    path('my-product-sets/<name>/ratings/', views.MyProductsetsRating.as_view()),
    path('ratings/highlights/', views.HiglightRatingList.as_view()),
    path('ratings/highlights/<pk>/', views.HighlightRating.as_view()),
    path('my-product-sets/<name>/', views.MyProductsetsDetail.as_view()),

    path('my-products/', views.MyProducts.as_view()),
    path('my-distributors/', views.MyDistributors.as_view()),
    path('my-distributors/add/<email>/', views.MyDistributorsAdd.as_view()),

    path('search/', views.SearchProducts.as_view()),
    path('statistics/', views.ManufacturerStats.as_view()),



    path('ratings/',views.Ratings.as_view()),
    path('ratings/<product_set_id>/',views.RatingsDetail.as_view()),
    path('ratings/<product_set_id>/stats/',views.RatingsStats.as_view()),
    
]
