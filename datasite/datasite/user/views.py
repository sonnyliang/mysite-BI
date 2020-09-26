
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
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self,request,*args,**kwargs):

        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }

        return Response(content)


        # ret = {'code':1000,'msg':None}
        # try:
        #     # 参数是datadict 形式
        #     usr = request.data.get('username')
        #     pas = request.data.get('password')

        #     # usr = request._request.POST.get('username')
        #     # pas = request._request.POST.get('password')

        #     # usr = request.POST.get('username')
        #     # pas = request.POST.get('password')


        #     obj = User.objects.filter(username=usr,password=pas).first()
        #     print(obj)

        #     if not obj:
        #         ret['code'] = '1001'
        #         ret['msg'] = '用户名或者密码错误'
        #         return JsonResponse(ret)
        #         # 这里为了简单，应该是进行加密，再加上其他参数
        #     token = str(time.time()) + usr
        #     print(token)
        #     User.userToken.objects.update_or_create(username=obj, defaults={'token': token})
        #     ret['msg'] = '登录成功'
        # except Exception as e:
        #     ret['code'] = 1002
        #     ret['msg'] = '请求异常'
        # return JsonResponse(ret)


# class UsersAPIView(ListCreateAPIView):
#     # 序列化类
#     serializer_class = UserSerializer
#     # 查询集和结果集
#     queryset = User.objects.all()
#     # 用户验证
#     authentication_classes = (UserAuth,)
#     # 权限控制
#     permission_classes = (Userpermission,)
#     # 直接进行权限控制permission (如上)b 
#     # 重写get请求，判断request.user 是否是UserModel中的一个实例
#     # def get(self, request, *args, **kwargs):
#     #     if isinstance(request.user, UserModel):
#     #         if request.user.is_super:
#     #             return self.list(request, *args, **kwargs)
#     #         else:
#     #             raise exceptions.NotAuthenticated  # 没有超级管理员的权限
#     #     else:
#     #         raise exceptions.NotAuthenticated   # 用户没有登录，没有权限访问

#     # 同一个post做把登录和注册同时完成
#     def post(self, request, *args, **kwargs):
#         action = request.query_params.get('action')
#         # 若参数为register则为注册，创建用户
#         if action == POST_ACTION_REGISTER:
#             return self.create(request, *args, **kwargs)
#         elif action == POST_ACTION_LOGIN:
#             # 验证用户名密码
#             u_name = request.data.get('u_name')
#             u_password = request.data.get('u_password')
#             try:
#                 user = UserModel.objects.get(u_name=u_name)   # 数据库验证用户名
#                 # 用户名存在验证密码
#                 if user.u_password == u_password:
#                     # 生成令牌,传入客户端和放入服务器缓存或者数据库
#                     token = uuid.uuid4().hex
#                     # 把token放入缓存,注意Redis在settings中的配置
#                     cache.set(token, user.id)
#                     # 并传入客户端
#                     data = {
#                         'msg': 'ok',
#                         'status': 200,
#                         'token': token
#                     }
#                     return Response(data)
#                 else:
#                     raise exceptions.AuthenticationFailed   # 用户密码错误
#             except UserModel.DoesNotExist:
#                 raise exceptions.NotFound   # 用户名错误
#         else:
#             raise exceptions.ValidationError  # 验证错误，传入的不是POST请求

#     # 创建用户
#     # 重写的CreateModelMixin中的方法：用于用户的创建
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)

#         data = serializer.data
#         u_name = data.get('u_name')
#         # 判断是否是创建的超级用户
#         if u_name in SUPER_USERS:
#             u_id = data.get('id')
#             user = UserModel.objects.get(pk=u_id)  # 拿到对应的用户
#             user.is_super = True  # 设置为超级用户o0
#             user.save()
#             data.update({'is_super': True})     # 创建了超级用户，在返回客户端的时候也把对应修改做了

#         headers = self.get_success_headers(data)
#         return Response(data, status=status.HTTP_201_CREATED, headers=headers)
