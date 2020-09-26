import django_filters
from .models import todoList

class todoListFilter(django_filters.FilterSet):
    class Meta():
        model = todoList
        fields =['user','todoType']