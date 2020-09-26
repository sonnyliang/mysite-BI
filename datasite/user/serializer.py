# serializers.py
# 用户序列化
from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 要显示出来的字段
        fields = ('id', 'username', 'password', 'is_superuser')
