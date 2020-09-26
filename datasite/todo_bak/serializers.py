from rest_framework import serializers
from .models import todoList


class todoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = todoList
        fields = [
            'username',
            'todo',
            'todoType',
            'create_time',
            'update_time',
        ]