from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductListCreateAPIView.as_view()),
    path("products/info/", views.ProductsInfoAPIView.as_view()),
    path("product_detail/<int:product_id>/", views.ProductDetailAPIView.as_view()),
    path("orders/", views.OrderListAPIView.as_view()),
    path("user-orders/", views.UserOrderListAPIView.as_view(), name="user-orders"),
]
