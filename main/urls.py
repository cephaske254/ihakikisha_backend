from django.urls import path, include
from . import views

urlpatterns = [
    path('add_product-set/',views.AddProductSet.as_view(),name='add_set'),
    path('delete_product-set/<pk>/',views.DeleteProductSet.as_view(),name='delete_set'),
    path('update_product-set/<pk>/',views.UpdateProductSet.as_view(),name='update_set'),
    path('all_product-sets/',views.AllProductSets.as_view(),name='view_all_set'),
    path('get_product-set/<pk>/',views.GetProductSet.as_view(),name='get_set'),
    path('update_products/<pk>/',views.UpdateProduct.as_view(),name='add_product'),
    path('get_product/<pk>/',views.GetProduct.as_view(),name='get_product'),
    path('all_products/',views.AllProducts.as_view())
]