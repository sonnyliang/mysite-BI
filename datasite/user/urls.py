from django.contrib import admin
from django.urls import path, include
from .views import UserView,LoginView, AuthView
from django.conf.urls import url

app_name="user"

urlpatterns =[
    path('', UserView),
    path('login/', LoginView, name="login"),
    url('auth/', AuthView.as_view()),
]