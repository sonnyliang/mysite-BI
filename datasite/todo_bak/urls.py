from django.urls import include, path
from . import views
from .views import getList


from rest_framework import routers

app_name = 'todo'

router = routers.DefaultRouter()
urlpatterns = [

    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('api/todoList/', getList.as_view()),
    
]