from django.contrib import admin
from django.urls import path


from shop.views import product_list, detail, add_product, edit_product, delete_product, login, products_of_category, \
    register

urlpatterns = [
    path('home/', product_list, name='home'),
    path("product-detail/<int:product_id>", detail, name="detail"),
    path('add-product/', add_product, name='add-product'),
    path('product/<int:product_id>/delete', delete_product, name='delete'),
    path('login/', login, name='login'),
    path('edit/<int:product_id>', edit_product, name='edit'),
    path('category/<int:category_id>/products', products_of_category, name='products_of_category'),
    path('register/', register, name='register'),
]