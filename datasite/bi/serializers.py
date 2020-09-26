from rest_framework import serializers
from .models import BusinessOrder, testSalesVolumn
 
class BusinessOrderListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BusinessOrder
        fields = [
            'billno',
            'billdate1',
            'vipcardno',
            'amount',
            'qty',
            'goodsname',
            'brand',
        ]

class testSalesVolumnListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = testSalesVolumn
        fields = [
            'billdate',
            'amount',
        ]
