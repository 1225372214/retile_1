import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a=open(r'D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task1_x2.csv',encoding='utf-8')
task1_x2=pd.read_csv(a)
data_Dept=task1_x2["Dept"].value_counts()
print(data_Dept,data_Dept.shape) #查看Dept的种类数目
task1_x2['Date'] = pd.to_datetime(task1_x2['Date'])
task1_x2['year']=[i.year for i in task1_x2['Date']] # 提取年份
task1_x2['month']=[i.month for i in task1_x2['Date']]# 提取月份
task1_x2['weekday'] = task1_x2['Date'].apply(lambda x: x.weekday()+1) # 提取星期
task1_x2['day']=[i.day for i in task1_x2['Date']] # 提取天
task1_x2['hour'] = task1_x2['Date'].dt.hour # 提取时
#data_1s=task1_x2.loc[task1_x2['Dept']=='第一食堂']
#print(data_1s)

#绘制早餐饼图
morning = []
for i in ['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']:
    b= task1_x2.loc[(task1_x2['Dept'] == i), :]
    c = b.loc[(b['hour'].apply(lambda x: x in [6, 7, 8])), :]#设定6-8点为早餐时间
    d = pd.pivot_table(c[['day', 'CardNo', 'Money']], index=c[['day', 'CardNo']], aggfunc = np.sum)
    morning.append(d.shape[0])
print('早餐各食堂就餐情况：\n',morning)

plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(6, 6))
label=['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']
explode=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
plt.title('各食堂早餐就餐人次的占比饼图')
plt.pie(morning, explode=explode, labels=label, autopct='%1.1f%%')
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_X1.png')
plt.show()
#绘制午餐饼图
noon = []
for i in ['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']:
    b= task1_x2.loc[(task1_x2['Dept'] == i), :]
    c = b.loc[(b['hour'].apply(lambda x: x in [11, 12, 13])), :]#设置11-13为午餐时间
    d = pd.pivot_table(c[['day', 'CardNo', 'Money']], index=c[['day', 'CardNo']], aggfunc = np.sum)
    noon.append(d.shape[0])
print('午餐各食堂就餐情况：\n',noon)


plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(6, 6))
label=['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']
explode=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
plt.title('各食堂午餐就餐人次的占比饼图')
plt.pie(noon, explode=explode, labels=label, autopct='%1.1f%%')
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_X2.png')
plt.show()
#绘制晚餐饼图
night = []
for i in ['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']:
    b= task1_x2.loc[(task1_x2['Dept'] == i), :]
    c = b.loc[(b['hour'].apply(lambda x: x in [17,18,19])), :]#设置17-19点为晚餐时间
    d = pd.pivot_table(c[['day', 'CardNo', 'Money']], index=c[['day', 'CardNo']], aggfunc = np.sum)
    night.append(d.shape[0])
print('晚餐各食堂就餐情况：\n',night)

plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(6, 6))
label=['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']
explode=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
plt.title('各食堂晚餐就餐人次的占比饼图')
plt.pie(night, explode=explode, labels=label, autopct='%1.1f%%')
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_X3.png')
plt.show()

