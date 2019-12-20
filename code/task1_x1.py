import pandas as pd
import numpy as np
import datetime
from pandas import Series,DataFrame,np
data_1=pd.read_csv(open(r'D:/我的资料库/Documents/Downloads/校园消费（实习）/data1.csv'),encoding='utf-8')
print("data1的数据分布情况:\n",data_1.describe())
data_2=pd.read_csv(open(r'D:/我的资料库/Documents/Downloads/校园消费（实习）/data2.csv'),encoding='utf-8')
print("data2的数据分布情况:\n",data_2.describe())
p1=DataFrame(data_1)
p2=DataFrame(data_2)
data_11=p1.dropna(axis=1)#去除缺失值的列
data_22=p2.dropna(axis=1)
print("data1数据缺失情况：\n",data_11.isnull().sum())
print("data2数据缺失情况：\n",data_22.isnull().sum())
print(data_11.shape)#计算出表格的行列数值
print(data_11.columns)#展示表格列的内容
print(data_22.shape)
print(data_22.columns)
##转换时间类型
data_222=data_22.copy()
print("使用read_csv读取的信息表的长度为：", len(data_222))
data_222['Date']= pd.to_datetime(data_222['Date'])
print('进行转换后表的类型为：\n',  data_222['Date'].dtypes)
year = [i.year for i in data_222['Date']]## 提取年份信息
month = [i.month for i in data_222['Date']]## 提取月份信息
day = [i.day for i in  data_222['Date']]## 提取日期信息
week = [i.week for i in  data_222['Date']]## 提取周信息
weekday = [i.weekday() for i in  data_222['Date']]##提取星期信息
weekname = [i.weekday_name for i in data_222['Date']]## 提取星期名称信息
#day=data_222['day']=data_222['Date'].dt.day   # 提取天
hour=data_222['hour'] = data_222['Date'].dt.hour  # 提取时
minute=data_222['minute'] = data_222['Date'].dt.minute  # 提取分
timemin = data_222['Date'].min()
timemax =data_222['Date'].max()
print('订单最早的时间为：',timemin)
print('订单最晚的时间为：',timemax)

df_2=data_222.loc[data_222['hour']>=5]##去除消费时间小于5的异常时间
df_2.to_csv('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task1_x2.csv',encoding='utf-8')
data_11.to_csv('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task1_x1.csv',encoding='utf-8')
#合并数据
data_mer=pd.merge(data_11,df_2,left_on='CardNo',right_on='CardNo',how='inner')
data_mer.to_csv('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task1_x3.csv',encoding='utf-8')
print('合并后数据形状',data_mer.shape)







