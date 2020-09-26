from db.base_model import BaseModel  #引入后自动新增创建时间、更新时间及删除标记
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息表'

class userToken(models.Model):
    username = models.OneToOneField(to='User',on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=60)

    class Meta:
        db_table =  'user_token'
        verbose_name = verbose_name_plural = '用户token表'
