import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a=open(r'D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task1_x2.csv',encoding='utf-8')
task1_x2=pd.read_csv(a)
task1_x2['Date'] = pd.to_datetime(task1_x2['Date'])
task1_x2['year']=[i.year for i in task1_x2['Date']] # 提取年份
task1_x2['month']=[i.month for i in task1_x2['Date']]# 提取月份
task1_x2['weekday'] = task1_x2['Date'].apply(lambda x: x.weekday()+1) # 提取星期
task1_x2['day']=[i.day for i in task1_x2['Date']] # 提取天
task1_x2['hour'] = task1_x2['Date'].dt.hour # 提取时

task1_x2x=task1_x2.loc[task1_x2['day']!=5]##提出5号清明假期
workdayss = []
for i in ['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']:
    b= task1_x2x.loc[(task1_x2x['Dept'] == i), :]
    c = task1_x2x.loc[(task1_x2x['weekday'].apply(lambda x: x in range(1, 6))), :]
    d = c.loc[:, ['hour', 'Money']]
    workdayss = d.groupby('hour').sum()
print('工作日就餐时间情况：\n',workdayss)
wuyi=task1_x2.loc[task1_x2['day']==28]##提出五一调休
nworkdays_5 = []
for i in ['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']:
    bb=wuyi.loc[(wuyi['Dept'] == i), :]
    dd=bb.loc[:, ['hour', 'Money']]
    workdays_5 = dd.groupby('hour').sum()
print('五一调休就餐时间情况：\n',workdays_5.shape)

workdays=pd.concat([workdays_5,workdayss],axis=0)###合并工作日时间
workdaysss = workdays.groupby('hour').sum()
print('非工作日就餐时间情况：\n',workdaysss)
#workdaysss.to_csv('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_x6.csv',encoding='utf-8')

workdaysss.to_csv('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_x4.csv',encoding='utf-8')


##绘制工作日就餐时间曲线图
df = open(r'D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_x4.csv',encoding='utf-8')
data2 = pd.read_csv(df)
x = data2.iloc[:, 0]
y = data2.iloc[:, 1]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
plt.title('工作日食堂就餐时间曲线图')
plt.xlabel('hour')  # 设置x轴标签
plt.ylabel('money')  # 设置y轴标签
plt.xticks(range(24))
plt.plot(x, y)
plt.legend()
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_X5.png')
plt.show()

task1_x2s=task1_x2.loc[task1_x2['day']!=28]##提出28号调休日
nonworkdays_s = []
for i in ['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']:
    b= task1_x2s.loc[(task1_x2['Dept'] == i), :]
    c = task1_x2s.loc[(task1_x2['weekday'].apply(lambda x: x in range(6, 8))), :]
    d = c.loc[:, ['hour', 'Money']]
    nonworkdays_s = d.groupby('hour').sum()
print('周六日工作日就餐时间情况：\n',nonworkdays_s)

qingming=task1_x2.loc[task1_x2['day']==5]##提出5号清明假期日
nonworkdays_5 = []
for i in ['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂','教师食堂']:
    bb=qingming.loc[(qingming['Dept'] == i), :]
   # c = task1_x2.loc[(task1_x2['weekday'].apply(lambda x: x in range(6, 7))), :]
    dd=bb.loc[:, ['hour', 'Money']]
    nonworkdays_5 = dd.groupby('hour').sum()
print('清明节就餐时间情况：\n',nonworkdays_5.shape)

nonworkdays=pd.concat([nonworkdays_5,nonworkdays_s],axis=0)###合并工作日时间
nonworkdaysss =nonworkdays.groupby('hour').sum()
print('非工作日就餐时间情况：\n',nonworkdaysss)
nonworkdaysss.to_csv('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_x6.csv',encoding='utf-8')


#绘制非工作日的就餐时间曲线图
data= open(r'D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_x6.csv',encoding='utf-8')
data2 = pd.read_csv(data)
x = data2.iloc[:, 0]
y = data2.iloc[:, 1]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
plt.title('非工作日食堂就餐时间曲线图')
plt.xlabel('hour')  # 设置x轴标签
plt.ylabel('money')  # 设置y轴标签
plt.xticks(range(24))
plt.plot(x, y)
plt.legend()
plt.savefig('D:/我的资料库/Documents/Downloads/校园消费（实习）/result/task2_X7.png')
plt.show()



