from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("product_detail/<int:id>", views.product_detail),
]
