from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
 
from .models import BusinessOrder, testSalesVolumn
from .serializers import BusinessOrderListSerializer, testSalesVolumnListSerializer

from .filter import BusinessOrderFilter, testSalesVolumnFilter


from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny


# 解析器
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import JSONParser


# Create your views here.

from urllib import parse

from django.http import HttpResponse
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

from .dataprocess import getsqldata

from django_pivot import pivot

from django.db.models import Q
from django.db.models import Count



class VueTest(ListAPIView):

    serializer_class = BusinessOrderListSerializer
    queryset = BusinessOrder.objects.filter(amount__gte=1000)
    
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
    filter_class = BusinessOrderFilter

class VolumnTest(APIView):

    serializer_class = testSalesVolumnListSerializer
    queryset = testSalesVolumn.objects.all()

    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
    filter_class = testSalesVolumnFilter


class ParamTest(APIView):

    def get(self, request, *args, **kwargs):


        params = dict(request.query_params)

        print(params)


        pivot_col='brand'
        pivot_row='billdate1'
        pivot_value='amount'

        brand = params['brand'][0]
        startDate = params['startDate'][0]
        endDate = params['endDate'][0]

        brand_list=['CHJ','FION','VENTI','CH']
        if params['brand'][0] !='ALL':
            brand_list=[]
            brand_list.append(params['brand'][0])

        if params['col'][0] =='品牌':
            pivot_col='brand'
        elif params['col'][0] =='大区':
            pivot_col='parentname'
        
        if params['row'][0] =='订单日期':
            pivot_row='billdate1'
        
        if params['value'][0] =='销售额':
            pivot_value='amount'
            django_pivot = pivot.pivot(BusinessOrder.objects.filter( Q(billdate1__gte=startDate) & Q(billdate1__lte=endDate) & Q(brand__in=brand_list) ), pivot_col, pivot_row,pivot_value)
        elif params['value'][0] =='消费人数':
            pivot_value='vipcardno'
            django_pivot = pivot.pivot(BusinessOrder.objects.filter( Q(billdate1__gte=startDate) & Q(billdate1__lte=endDate) & Q(brand__in=brand_list) ), pivot_col, pivot_row,pivot_value,aggregation=Count )
        
        return Response(django_pivot)


# class VolumnTest(APIView):
#     parser_classes = [JSONParser, ]  # 解析类

#     def get(self, request, *args, **kwargs):

#         print(request.query_params)

#         params = dict(request.query_params)

#         result =getsqldata(params)
        
        
#         return Response(result)

    



# 本地测试
# SQLALCHEMY_DATABASE_URL = 'mssql+pymssql://model:123456@192.168.16.222/cdp_hy'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)  #创建数据库连接引擎

# 服务器
SQLALCHEMY_DATABASE_URL = 'mssql+pymssql://CHJIT:chj_itW#Jwadfse@1i*3isn_wie3@119.23.45.248/TestService'
engine = create_engine('mssql+pymssql://CHJIT:%s@119.23.45.248/TestService'%parse.unquote_plus('chj_itW#Jwadfse@1i*3isn_wie3'))




# 取数SQL
def sqlparse(start_date, end_date, brand, filter_sql=None):
    sql = "Select * from %s Where BILLDATE1 BETWEEN '%s' AND '%s' And BRAND = '%s'"% ('Business_order', start_date, end_date, brand) # 必选的两个筛选字段
    if filter_sql is not None:
        sql = "%s And %s" % (sql, filter_sql) # 其他可选的筛选字段，如有则以And连接自定义字符串
    return sql



def kpi(df):
    # 市场按列求和，最后一行（最后一个DATE）就是最新的市场规模
    market_size = df.sum(axis=1).iloc[-1]
    # 市场按列求和，倒数第5行（倒数第5个DATE）就是同比的市场规模，可以用来求同比增长率
    market_gr = df.sum(axis=1).iloc[-1] / df.sum(axis=1).iloc[-5] - 1
    # 因为数据第一年是四年前的同期季度，时间序列收尾相除后开四次方根可得到年复合增长率
    market_cagr = (df.sum(axis=1).iloc[-1] / df.sum(axis=1).iloc[0]) ** (0.25) - 1
    if market_size == np.inf or market_size == -np.inf:
        market_size = 'N/A'
    if market_gr == np.inf or market_gr == -np.inf:
        market_gr = 'N/A'
    if market_cagr == np.inf or market_cagr == -np.inf:
        market_cagr = 'N/A'
        
    return [market_size, market_gr, market_cagr]


# 该字典key为前端准备显示的所有多选字段名, value为数据库对应的字段名
D_FIELD = {
    '品牌': '[BRAND]',
    '日期': '[BILLDATE1]',
    '大区': '[PARENTNAME]',
}


def index(request):
    # sql = "Select count(*) from BUSINESS_ORDER_HY" #标准sql语句，此处为测试返回数据库data表的数据条目n，之后可以用python处理字符串的方式动态扩展
    sql = sqlparse('2019-05-01','2019-06-01','CHJ')
    df = pd.read_sql_query(sql, engine) #将sql语句结果读取至Pandas Dataframe

    pivoted = pd.pivot_table(df,
                       values='AMOUNT',  # 数据透视汇总值为AMOUNT字段，一般保持不变
                       index='BILLDATE1',  # 数据透视行为BILLDATE1字段，一般保持不变
                       columns='SHOPCODE',  # 数据透视列为SHOPCODE字段，该字段以后应跟随分析需要动态传参
                       aggfunc=np.sum) # 数据透视汇总方式为求和，一般保持不变
    
    mselect_dict = {}
    for key, value in D_FIELD.items():
        mselect_dict[key] = {}
        mselect_dict[key]['select'] = value
        # mselect_dict[key]['options'] = option_list 以后可以后端通过列表为每个多选控件传递备选项


    context  ={
        'market_size': kpi(pivoted)[0],
        'market_gr': kpi(pivoted)[1],
        'market_cagr': kpi(pivoted)[2],
        'mselect_dict': mselect_dict
    }
    # return HttpResponse(df.to_html()) #渲染，这里暂时渲染为最简单的HttpResponse，以后可以扩展
    return render(request, 'display.html',context)

