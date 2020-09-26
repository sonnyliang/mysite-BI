from django.db import models


# Create your models here.

class todoList(models.Model):
    user = models.CharField(max_length=256)
    todo = models.CharField(max_length=256)
    todoType = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        managed = False
        db_table = 'todoList'

