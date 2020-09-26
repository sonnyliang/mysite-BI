from django.shortcuts import render

from .models import todoList
from .filter import todoListFilter
from .serializers import todoListSerializer


from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny





# Create your views here.
class getList(ListAPIView):

    serializer_class = todoListSerializer
    queryset = todoList.objects.all()

    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
    filter_class = todoListFilter
