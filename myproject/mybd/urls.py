from django.urls import path 
from .views import ProductsOrder, ProductUpdate
 
urlpatterns = [ 
    path('products_order/', ProductsOrder.as_view(), name='products_order'),
    path('product/update/', ProductUpdate.as_view(), name='product_update')
    #path('about/', views.about, name='about'), 
] 