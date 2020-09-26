from django.shortcuts import render
from rest_framework.response import Response

from .models import todoList
from .filter import todoListFilter
from .serializers import todoListSerializer


from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from rest_framework import mixins, viewsets


# Create your views here.
# class getList(ListAPIView):

#     serializer_class = todoListSerializer
#     queryset = todoList.objects.all()

#     pagination_class = PageNumberPagination
#     permission_classes = [AllowAny]
#     filter_class = todoListFilter

class getList(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin):

    queryset = todoList.objects.all()
    serializer_class = todoListSerializer

class addTodo(APIView):

    def post(self, request, *args, **kwargs):

        params = dict(request.query_params)

        add_todo = todoList.objects.create(user=params['user'][0], todo=params['todo'][0], todoType=params['todoType'][0])

        add_todo.save()

        return Response('成功添加')

