from django.contrib import admin
from django.urls import path


from shop.views import product_list, detail, add_product, edit_product, delete_product, login_page, \
    products_of_category, register_page, add_order, add_comment

urlpatterns = [
    path('home/', product_list, name='home'),
    path("product-detail/<int:product_id>", detail, name="detail"),
    path('add-product/', add_product, name='add-product'),
    path('product/<int:product_id>/delete', delete_product, name='delete'),
    path('login/', login_page, name='login'),
    path('edit/<int:product_id>', edit_product, name='edit'),
    path('category/<int:category_id>/products', products_of_category, name='products_of_category'),
    path('register/', register_page, name='register'),
    path('product/<int:product_id>/new_order', add_order, name='add_order'),
    path('product/<int:product_id>/new_comment', add_comment, name='add_comment'),

]