import pandas as pd
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('data/exercise_data/train.csv')

# 计算每个乘客等级的生还率
survival_rates = df.groupby('Pclass')['Survived'].mean()

# 创建直方图
plt.figure(figsize=(10, 6))
survival_rates.plot(kind='bar')
plt.title('不同乘客等级的生还率')
plt.xlabel('乘客等级')
plt.ylabel('生还率')
plt.xticks(rotation=45)  # 添加横坐标旋转45度


# 在柱状图上添加具体数值
for i, rate in enumerate(survival_rates):
    plt.text(i, rate, f'{rate:.2%}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# 打印具体数值
print("\n各乘客等级的生还率：")
print(survival_rates.apply(lambda x: f"{x:.2%}"))

# 创建第二个图表：分析年龄与生还率的关系
plt.figure(figsize=(12, 6))

# 将年龄分组，使用更细致的分组
df['AgeGroup'] = pd.cut(df['Age'],
                       bins=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 80],
                       labels=['0-5', '6-10', '11-15', '16-20', '21-25',
                              '26-30', '31-35', '36-40', '41-45', '46-50',
                              '51-55', '56-60', '60+'])

# 计算每个年龄组的人数和生还人数
age_stats = df.groupby('AgeGroup').agg({
    'Survived': ['count', 'sum', 'mean']
})
age_stats.columns = ['总人数', '生还人数', '生还率']

# 绘制年龄组生还率的直方图
plt.subplot(2, 1, 1)
age_stats['生还率'].plot(kind='bar', color='skyblue')
plt.title('不同年龄组的生还率')
plt.xlabel('年龄组')
plt.ylabel('生还率')
plt.xticks(rotation=45)  # 添加横坐标旋转45度

# 在柱状图上添加具体数值
for i, rate in enumerate(age_stats['生还率']):
    plt.text(i, rate, f'{rate:.2%}', ha='center', va='bottom')

# 添加人数分布图
plt.subplot(2, 1, 2)
age_stats['总人数'].plot(kind='bar', color='lightgreen')
plt.title('不同年龄组的人数分布')
plt.xlabel('年龄组')
plt.ylabel('人数')
plt.xticks(rotation=45)  # 添加横坐标旋转45度

# 在柱状图上添加具体数值
for i, count in enumerate(age_stats['总人数']):
    plt.text(i, count, str(int(count)), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# 打印详细统计信息
print("\n各年龄组的统计信息：")
print(age_stats.round(3))
