from django.urls import include, path
from . import views
from .views import VueTest, ParamTest, VolumnTest

from rest_framework import routers

app_name = 'bi'

router = routers.DefaultRouter()
urlpatterns = [
    path('index/', views.index, name='index'),

    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('api/test/', VueTest.as_view()),
    path('api/paramtest/', ParamTest.as_view()),
    path('api/volumntest/', VolumnTest.as_view()),
    
]