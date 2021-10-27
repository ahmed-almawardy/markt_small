from order.models import (Product, Order)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView
    )

from order import serializers


class ConfigProduct:
    queryset = Product.objects.all()


class Create(ConfigProduct, CreateAPIView):
    serializer_class = serializers.ProductSerializerWrite
    

class Get(ConfigProduct, RetrieveAPIView):
    serializer_class = serializers.ProductSerializerRead


class List(ConfigProduct, ListAPIView):
    serializer_class = serializers.ProductSerializerRead


class Update(ConfigProduct, UpdateAPIView):
    serializer_class = serializers.ProductSerializerWrite


class DeleteOne(ConfigProduct, DestroyAPIView):
    ...


class ConfigOrder:
    queryset = Order.objects.all()


class CreateOrder(ConfigOrder, CreateAPIView):
    serializer_class = serializers.OrderSerializerCreate


class GetOrder(ConfigOrder, RetrieveAPIView):
    serializer_class = serializers.OrderSerializerRead


class ListOrder(ConfigOrder, ListAPIView):
    serializer_class = serializers.OrderSerializerRead


class UpdateOrder(ConfigOrder, UpdateAPIView):
    serializer_class = serializers.OrderSerializerCreate


class DeleteOneOrder(ConfigOrder, DestroyAPIView):
    ...
