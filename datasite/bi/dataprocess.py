from urllib import parse

from django.http import HttpResponse
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

# 本地测试
# SQLALCHEMY_DATABASE_URL = 'mssql+pymssql://model:123456@192.168.16.222/cdp_hy'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)  #创建数据库连接引擎

# 服务器
SQLALCHEMY_DATABASE_URL = 'mssql+pymssql://CHJIT:chj_itW#Jwadfse@1i*3isn_wie3@119.23.45.248/TestService'
engine = create_engine('mssql+pymssql://CHJIT:%s@119.23.45.248/TestService'%parse.unquote_plus('chj_itW#Jwadfse@1i*3isn_wie3'))




# 取数SQL
def sqlparse(start_date, end_date, brand):
    sql = "Select billdate1, sum(amount) '销售额' from %s Where BILLDATE1 BETWEEN '%s' AND '%s' And BRAND = '%s' GROUP BY billdate1"% ('Business_order', start_date, end_date, brand) 
    
    return sql



def getsqldata(params):

    # brand=params['brand'][0]
    # start_date=params['start_date'][0]
    # end_date = params['end_date'][0]

    sql ="Select billdate1, sum(isnull(cast(amount as decimal(15,1)),0)) 'sum_amount' from Business_order Where BILLDATE1 BETWEEN '2020-05-01' AND '2020-05-30' And BRAND = 'chj' GROUP BY billdate1"
    
    # sql = sqlparse('2019-05-01','2019-06-01','CHJ')

    df = pd.read_sql_query(sql, engine) #将sql语句结果读取至Pandas Dataframe

    result = df.to_json(orient='records')

    return result