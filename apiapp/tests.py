import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from apiapp.models import Products
from apiapp.serializers import ProductsSerializers
factory = APIRequestFactory()



class ProductsTestCase(APITestCase):
    def test_add(self):
        data = {'name':'tênis'}
        response = self.client.post("/apiapp/rest-auth/products/",data)
        request = factory.post('/products/', data, format='json')
     
     
    def test_get(self):
        request = factory.get('/products/')


class ProductImagesTestCase(APITestCase):
    def test_add(self):
        data = {'name':'tênis'}
        response = self.client.post("/apiapp/rest-auth/products/",data)
        request = factory.post('/product-images/', data, format='json')
     
    
    def test_get(self):
        request = factory.get('/products-images/')
