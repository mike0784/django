from django.urls import path 
from .views import ProductsOrder
 
urlpatterns = [ 
    path('products_order/', ProductsOrder.as_view(), name='products_order'), 
    #path('about/', views.about, name='about'), 
] 