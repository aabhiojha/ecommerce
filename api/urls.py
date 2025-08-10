from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductListAPIView.as_view()),
    path("product/info/", views.product_info),
    path("product_detail/<int:product_id>/", views.ProductDetailAPIView.as_view()),
    path("orders/", views.OrderListAPIView.as_view()),
    path("user-orders/", views.UserOrderListAPIView.as_view(), name="user-orders"),
]
