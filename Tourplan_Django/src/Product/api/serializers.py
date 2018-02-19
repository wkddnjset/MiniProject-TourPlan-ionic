from rest_framework import serializers
from Product.models import ProductList

class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = [
            'id',
            'img_url',
            'title',
            'sub_title',
        ]