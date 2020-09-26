
from django.contrib import auth
from django.shortcuts import redirect, render
from django.urls import reverse

import time
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import authentication
from rest_framework import exceptions


def UserView(request):
    context ={}
    return render(request, 'login.html',context)

def LoginView(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    user = auth.authenticate(request, username=username, password=password)

    # 获取请求的页面地址，如果无则返回首页
    # referer = request.META.get('HTTP_REFERER',reverse('index')) #将首页别名 home 反向解析成正常的链接

    if user is not None:
        auth.login(request, user)
        # Redirect to a sucess page
        return render(request, 'index.html')  #登录成功后返回到原来页面
    else:
        return render(request, 'error.html',{'message':'用户名或密码不正确'})



class AuthView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,]

    def get(self,request,*args,**kwargs):

        print(request.user)

        content = {
            # 'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            # 'auth': unicode(request.auth),  # None
            'user': str(request.user).encode('unicode_escape').decode(),
            'auth': str(request.auth).encode('unicode_escape').decode()
        }

        return Response(content)

