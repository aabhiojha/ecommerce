from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Order, OrderItem, Product
from api.serializers import OrderSerializer, ProductSerializer


@api_view(["GET"])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(["GET"])
def order_list(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)
