import pandas as pd
from pandas import Series,DataFrame
import numpy as np

df=open(r'D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task1_x3.csv',encoding='utf-8')
data=pd.read_csv(df)
##Money月消费总额、FundMoney月储存金额、消费地点等指标建立模型
index=['第一食堂','第二食堂','第三食堂','第四食堂','第五食堂','好利来食品店','红太阳超市','教师食堂','水电缴费处']
data_1 = data.loc[data['Dept'].isin(index)]
Index=['财务处','医务室','第二图书馆','第一图书馆','工商系部','自然科学书库','财务部','第七教学楼',
       '艺术设计学院','第六教学楼','人文社科','第五教学楼','飞凤轩宿管办','机电系 ','基础课部 ','第四教学楼',
       '第三教学楼','宿管办','财经系','第一教学楼','青鸾苑宿管办','外语系','旅游系']
data_2 = data.loc[data['Dept'].isin(Index)]
data_RFM1=data_1.groupby('CardNo').agg({'Money':'sum'})
data_RFM1.rename(columns={"CardNo":"CardNo","Money":"生活饮食消费"},inplace=True)
data_RFM2=data_2.groupby('CardNo').agg({'Money':'sum','FundMoney':'sum'})
data_RFM2.rename(columns={"CardNo":"CardNo","Money":"其他消费","FundMoney":"存款"},inplace=True)
a=DataFrame(data_RFM1)
b=DataFrame(data_RFM2)
data_1=a.fillna(0)#填充缺失值为0
data_2=b.fillna(0)
data_RFM=pd.concat([data_1,data_2],axis=1)
print(data_RFM)
print ('-' * 60)

recency_value = data_1['生活饮食消费'].groupby(data_1.index).sum()
frequency_value = data_2['其他消费'].groupby(data_2.index).sum()
monetary_value = data_2['存款'].groupby(data_2.index).sum()
# 计算RFM得分
# 分别计算R、F、M得分
r_score = pd.cut(recency_value, 5, labels=[1,2,3,4,5])  # 计算R得分
f_score = pd.cut(frequency_value, 5, labels=[5,4,3,2,1])  # 计算F得分
m_score = pd.cut(monetary_value, 5, labels=[1,2,3,4,5])  # 计算M得分

# R、F、M数据合并
rfm_pd=pd.concat([r_score, f_score, m_score],axis=1)
print ('得分情况\n',rfm_pd)
print ('-' * 60)
# 计算RFM总得分
rfm_pd['综合']= np.sum(rfm_pd,axis=1)
print(rfm_pd)
rfm_pd.to_csv('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task3_x4.csv')
###绘制散点图
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
#定义坐标轴
fig = plt.figure()
ax = plt.axes(projection='3d')
xs=rfm_pd.iloc[:,1]
ys=rfm_pd.iloc[:,2]
zs=rfm_pd.iloc[:,3]
ax.scatter(xs,ys,zs,c='c',marker='^')
ax.set_xlabel('生活饮食消费')
ax.set_ylabel('其他消费')
ax.set_zlabel('存款')
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task3_X5.png')
plt.show()