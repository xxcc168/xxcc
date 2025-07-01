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

# 在柱状图上添加具体数值
for i, rate in enumerate(survival_rates):
    plt.text(i, rate, f'{rate:.2%}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# 打印具体数值
print("\n各乘客等级的生还率：")
print(survival_rates.apply(lambda x: f"{x:.2%}"))

