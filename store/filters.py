import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    discraption = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name','price','Discountprice','ISNew','ISBestseller','discraption','category','Brand']