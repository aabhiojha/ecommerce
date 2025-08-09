from rest_framework import serializers

from api.models import Order, OrderItem, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "stock",
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price    must be greater than 0.")
        return value


class OrderItemSeraializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "product",
            "quantity",
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSeraializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "order_id",
            "created_at",
            "user",
            "status",
            "items",
        )
