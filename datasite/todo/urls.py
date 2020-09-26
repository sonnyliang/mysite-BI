from django.urls import include, path
from . import views
from .views import getList, addTodo
from .routers import StandardRouter

# from rest_framework import routers
from rest_framework.routers import SimpleRouter

app_name = 'todo'

# router = routers.DefaultRouter()
# router = SimpleRouter()
router = StandardRouter()

router.register('getTodo', getList)
urlpatterns = [

    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('api/todoList/', getList),
    path('api/addTodo', addTodo.as_view()),
    
]