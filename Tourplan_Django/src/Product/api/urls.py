from .views import ProductListView
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', ProductListView.as_view(), name='product-list'),
]