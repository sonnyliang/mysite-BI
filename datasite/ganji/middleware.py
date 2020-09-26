# 给ganji app 添加处理跨域问题的CORS响应的中间件，为了让vue项目能访问到
from django.utils.deprecation import MiddlewareMixin

class MyCorsMiddle(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] ='*'
        if response.method =='OPTIONS':
            response['Access-Control-Allow-Header'] ='*'
        return response