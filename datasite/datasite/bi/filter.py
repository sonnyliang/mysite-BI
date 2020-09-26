import django_filters
from .models import BusinessOrder, testSalesVolumn

class BusinessOrderFilter(django_filters.FilterSet):
    class Meta():
        model = BusinessOrder
        fields = ['brand', 'billdate1']

class testSalesVolumnFilter(django_filters.FilterSet):
    class Meta():
        model = testSalesVolumn
        fields = ['billdate']

