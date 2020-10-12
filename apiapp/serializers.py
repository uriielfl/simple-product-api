from rest_framework import serializers
from .models import Products 
from .models import ProductImages

class ProductsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name')

class ProductImagesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('productId', 'image', 'image_created_date')
        