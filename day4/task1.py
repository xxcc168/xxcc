# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt

# 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']

# 金牌个数
gold_medal = np.array([16, 12, 9, 8, 8])

# 银牌个数
silver_medal = np.array([8, 10, 4, 10, 5])

# 铜牌个数
bronze_medal = np.array([13, 5, 2, 7, 5])

# 创建x轴坐标
x = np.arange(len(countries))

# 设置x轴标签
plt.xticks(x, countries)

# 绘制条形图
plt.bar(x-0.2, gold_medal, width=0.2, color="gold")
plt.bar(x, silver_medal, width=0.2, color="silver")
plt.bar(x+0.2, bronze_medal, width=0.2, color="saddlebrown")

# 显示文本标签
# 金牌
for i in x:
    plt.text(x[i]-0.2, gold_medal[i], gold_medal[i],
             va='bottom', ha='center', fontsize=8)
# 银牌
for i in x:
    plt.text(x[i], silver_medal[i], silver_medal[i],
             va='bottom', ha='center', fontsize=8)
# 铜牌
for i in x:
    plt.text(x[i]+0.2, bronze_medal[i], bronze_medal[i],
             va='bottom', ha='center', fontsize=8)

plt.show()  # 显示图形