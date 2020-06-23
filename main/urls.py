from django.urls import path, include
from . import views

urlpatterns = [
    path('add_product-set/',views.AddProductSet.as_view(),name='add_set'),
    path('product-set/details/<pk>/',views.ProductSetDetails.as_view(),name='update_set'),
    path('add_products/',views.AddProduct.as_view(),name='add_product'),
    path('product/details/<pk>/',views.ProductDetails.as_view(),name='get_product'),
]

