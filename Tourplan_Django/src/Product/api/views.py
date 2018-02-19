from rest_framework import generics
from Product.models import ProductList
from .serializers import ProductListSerializers

class ProductListView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ProductListSerializers
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return ProductList.objects.all()