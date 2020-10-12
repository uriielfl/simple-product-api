from rest_framework import viewsets
from .serializers import ProductsSerializers
from .serializers import ProductImagesSerializers
from .models import Products
from .models import ProductImages
from rest_framework import status   
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse


class ProductsViewSet(viewsets.ModelViewSet, APIView):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializers  

   
   
class ProductImagesViewSet(viewsets.ModelViewSet):
    queryset = ProductImages.objects.all().order_by('id')
    serializer_class = ProductImagesSerializers
