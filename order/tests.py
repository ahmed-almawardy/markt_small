from django.http import response
from django.test import TestCase
from django.urls.base import reverse_lazy
from django.urls.conf import path
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient

from order.testHelper import (ORDER_DATA, PRODUCT_DATA, create_order, create_product, ORDER_DATA_NEW)
from user.testHelpers import create_user
from order.common import format_price

class OrderTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = create_user() 

    def create_order(self):
        return create_order(user=self.user, products=[self.product, self.product_two, self.product_three])

    def test_product_create(self):
        url = reverse_lazy('order:product-create')
        response = self.client.post(data=PRODUCT_DATA, path=url)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
    
    def test_product_put(self):
        self.product = create_product() 
        url = reverse_lazy('order:product-update', args=[self.product.id])
        response = self.client.put(data=PRODUCT_DATA, path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)
    
    def test_product_patch(self):
        self.product = create_product() 
        url = reverse_lazy('order:product-update', args=[self.product.id])
        data =  {'title': 'new product name'}
        response = self.client.patch(data=data, path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)
    
    def test_product_delete(self):
        self.product = create_product() 
        url = reverse_lazy('order:product-delete', args=[self.product.id])
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_product_get(self):
        self.product = create_product() 
        url = reverse_lazy('order:product-get', args=[self.product.id])
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_product_list(self):
        self.product = create_product() 
        url = reverse_lazy('order:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_order_create(self):
        self.product = create_product() 
        self.product_two = create_product(name='water') 
        self.product_three = create_product(name='phone') 
        self.order = self.create_order()
        url = reverse_lazy('order:create')
        response = self.client.post(data=ORDER_DATA, path=url)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
    
    def test_order_sum(self):
        self.product = create_product() 
        self.product_two = create_product(name='water') 
        self.product_three = create_product(name='phone') 
        self.order = self.create_order()
        url = reverse_lazy('order:create')
        response = self.client.post(data=ORDER_DATA, path=url)
        # self.assertEqual(response.status_code, HTTP_201_CREATED)
        
        summation = float(self.product.price) + float(self.product_three.price)\
            +float(self.product_two.price)
        summation = format_price(summation)
        self.assertEqual(response.json()['price'], summation)

    def test_order_put(self):
        self.product = create_product() 
        self.product_two = create_product(name='water') 
        self.product_three = create_product(name='phone') 
        self.order = self.create_order()
        url = reverse_lazy('order:update', args=[self.order.id])
        response = self.client.put(data=ORDER_DATA_NEW, path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)
    
    def test_order_patch(self):
        self.product = create_product() 
        self.product_two = create_product(name='water') 
        self.product_three = create_product(name='phone') 
        self.order = self.create_order()
        url = reverse_lazy('order:update', args=[self.order.id])
        data =  {'title': 'new order name'}
        response = self.client.patch(data=data, path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)
    
    def test_order_delete(self):
        self.product = create_product() 
        self.product_two = create_product(name='water') 
        self.product_three = create_product(name='phone') 
        self.order = self.create_order()
        url = reverse_lazy('order:delete', args=[self.order.id])
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_order_get(self):
        self.product = create_product() 
        self.product_two = create_product(name='water') 
        self.product_three = create_product(name='phone') 
        self.order = self.create_order()
        url = reverse_lazy('order:get', args=[self.order.id])
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_order_list(self):
        self.product = create_product() 
        self.product_two = create_product(name='phone') 
        self.product_three = create_product(name='laptop') 
        self.order = self.create_order()
        url = reverse_lazy('order:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
