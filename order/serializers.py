from rest_framework import serializers 
from rest_framework.exceptions import APIException
from order.models import (
    Product,
    Order,
    ProductsOrder
)
from django.conf import settings
from order.common import format_price


class ProductSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'img',
            'price',
            'desc'
        )

    def update(self, instance, validated_data):
        self.reformate_price(validated_data)        
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        self.reformate_price(validated_data)        
        return super().create(validated_data)

    def price_validate(self, price):
        try:
            price = float(price)
        except ValueError:
            raise APIException('not a valid price')
    
    def reformate_price(self, validated_data):
        if validated_data.get('price'):
            self.price_validate(validated_data.get('price'))
            formated_price = format_price(validated_data.get('price'))
            validated_data['price'] = formated_price
            

class ProductSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price', 
            'img',
            'desc',
        )


# class ProductsOrderSerializerRead(serializers.ModelSerializer):
#     class Meta:
#         model = ProductsOrder
#         fields = (
#             'product',
#             ''
#         )

class OrderSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'title',
            'products',
            'user',
            'address',
            'price'
        )
        extra_kwargs = {
            'price': {'read_only': True}
        }

    def update(self, instance, validated_data):
        user = validated_data.get('user', instance.user)
        if not user == self.instance.user:
            raise APIException('you can\'t user after order created.')
        return super().update(instance, validated_data)

class OrderSerializerRead(serializers.ModelSerializer):
    user  = serializers.StringRelatedField()
    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Order
        fields = (
            'id',
            'products',
            'price',
            'user'
        )
    
    def create(self, validated_data):
        raise NotImplementedError()
    
    def update(self, instance, validated_data):
        raise NotImplementedError()
