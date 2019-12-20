import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=open(r'D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task1_x3.csv',encoding='utf-8')
data=pd.read_csv(df)
data_1=data['CardNo'].value_counts()
print('18级学生总人数:',data_1.count())##计算18级整体学生总人数
data_2=data['CardCount'].count()
print('本月人均刷卡频次：',data_2/data_1.count())
data_3=data['Money'].sum()
print('本月人均消费：',data_3/data_1.count())

###计算18级各专业人均消费
gb=data['Money'].groupby(data['Major']).sum()
total=data['CardNo'].groupby(data['Major']).value_counts()
total_1=total.count()
#print(gb,total_1)
z=gb/total_1
print('各专业消费情况：\n',z)
###绘制18级各专业人均消费条形图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
fig=plt.figure(figsize=(13,10))
y=z
x=y.index
plt.xticks(rotation=80)
plt.bar(x,y,width=0.5,color='bc')
plt.xlabel('Major')
plt.ylabel('Money')
plt.title('18级各专业四月人均消费情况')
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task3_X1.png')
plt.show()


Boys=data.loc[data['Sex']=='男']
Girls=data.loc[data['Sex']=='女']

###计算18级各专业男生人均消费
gb=Boys['Money'].groupby(Boys['Major']).sum()
total=Boys['CardNo'].groupby(Boys['Major']).value_counts()
total_1=total.count()
zz=gb/total_1
print('各专业男生消费情况：\n',zz)
###绘制18级各专业男生人均消费条形图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
fig=plt.figure(figsize=(13,10))
y=zz
x=y.index
plt.xticks(rotation=80)
plt.bar(x,y,width=0.5,color='gb')
plt.xlabel('Major')
plt.ylabel('Money')
plt.title('18级各专业男生四月人均消费情况')
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task3_X2.png')
plt.show()

###计算18级各专业女生人均消费
gb=Girls['Money'].groupby(Girls['Major']).sum()
total=Girls['CardNo'].groupby(Girls['Major']).value_counts()
total_1=total.count()
kk=gb/total_1
print('各专业女生消费情况：\n',kk)
###绘制18级各专业女生人均消费条形图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
fig=plt.figure(figsize=(13,10))
y=kk
x=y.index
plt.xticks(rotation=80)
plt.bar(x,y,width=0.5,color='my')
plt.xlabel('Major')
plt.ylabel('Money')
plt.title('18级各专业女生四月人均消费情况')
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task3_X3.png')
plt.show()



