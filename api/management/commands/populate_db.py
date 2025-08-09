import random
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from api.models import Order, OrderItem, Product, User


class Command(BaseCommand):
    help = "Creates application data"

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username="admin").first()
        if not user:
            user = User.objects.create_superuser(username="admin", password="test")

            # create products - name, desc, price, stock, image
            products = [
                Product(
                    name="Wireless Bluetooth Headphones",
                    description="Experience high-fidelity audio with noise-canceling technology and 30 hours of battery life.",
                    price=Decimal("89.99"),
                    stock=15,
                ),
                Product(
                    name="Stainless Steel Water Bottle",
                    description="Keeps your drinks cold for 24 hours or hot for 12 hours, perfect for outdoor adventures.",
                    price=Decimal("19.50"),
                    stock=40,
                ),
                Product(
                    name="Gaming Mechanical Keyboard",
                    description="RGB backlit mechanical keyboard with tactile switches for precision and speed.",
                    price=Decimal("65.75"),
                    stock=12,
                ),
                Product(
                    name="4K Ultra HD Smart TV",
                    description="Enjoy stunning visuals and vibrant colors with built-in streaming apps and voice control.",
                    price=Decimal("599.99"),
                    stock=5,
                ),
                Product(
                    name="Portable Power Bank",
                    description="10,000mAh fast-charging power bank with dual USB ports for charging multiple devices.",
                    price=Decimal("29.99"),
                    stock=25,
                ),
                Product(
                    name="Smart Fitness Watch",
                    description="Track your heart rate, steps, and workouts with a sleek, water-resistant design.",
                    price=Decimal("120.00"),
                    stock=8,
                ),
            ]

        # create products & re-fetch from DB
        Product.objects.bulk_create(products)
        products = Product.objects.all()

        # create some dummy orders tied to the superuser
        for _ in range(3):
            # create an Order with 2 order items
            order = Order.objects.create(user=user)
            for product in random.sample(list(products), 2):
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1, 3)
                )
