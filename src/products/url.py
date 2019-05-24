from products.views import product_detail_view
from products.views import product_create_view
from products.views import product_delete_view
from products.views import product_list_view
from django.urls import path

urlpatterns = [
    path('/<int:my_id>', product_detail_view, name='product'),
    path('/create', product_create_view, name='product_create'),
    path('', product_list_view),
    path('/delete/<int:my_id>', product_delete_view)
]