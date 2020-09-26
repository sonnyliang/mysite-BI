from django.urls import path, re_path
from . import views as ganji


urlpatterns = [
    re_path('', ganji.test),
]