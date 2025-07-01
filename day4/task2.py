import pandas as pd
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('生产总值.csv')

# 1. 绘制2015-2017年各个城市的国内生产总值的直方图
plt.figure(figsize=(10, 6))
cities = df['地区'].unique()
x = range(len(cities))
width = 0.25

# 获取各年份数据
data_2015 = df[df['年份']==2015]['国内生产总值'].values
data_2016 = df[df['年份']==2016]['国内生产总值'].values
data_2017 = df[df['年份']==2017]['国内生产总值'].values

# 绘制直方图
plt.bar(x, data_2015, width, label='2015年')
plt.bar([i+width for i in x], data_2016, width, label='2016年')
plt.bar([i+width*2 for i in x], data_2017, width, label='2017年')

plt.xlabel('城市')
plt.ylabel('国内生产总值（亿元）')
plt.title('2015-2017年各城市国内生产总值对比')
plt.xticks([i+width for i in x], cities)
plt.legend()
plt.show()

# 2. 绘制2015年各个城市的国内生产总值的饼状图
plt.figure(figsize=(8, 8))
data_2015 = df[df['年份']==2015]
plt.pie(data_2015['国内生产总值'], labels=data_2015['地区'],
        autopct='%1.1f%%', startangle=90)
plt.title('2015年各城市国内生产总值占比')
plt.axis('equal')
plt.show()

