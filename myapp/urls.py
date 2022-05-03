
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
      path('',views.home,name='home'),
    #   path('products/' , views.products,name="products"),
    #   path('products/<int:id>', views.product_detail,name='product_detail'),
    #   path('products/add/',views.add_product),
    #   path('products/update/<int:id>/',views.update_product,name='update_product'),
    #   path('products/delete/<int:id>/',views.delete_product,name='delete_product'),
]