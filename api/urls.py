from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("product/info/", views.product_info),
    path("product_detail/<int:id>", views.product_detail),
    path("orders/", views.order_list),
]
