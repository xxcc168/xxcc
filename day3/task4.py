import pandas as pd

def analyze_drinks():
    """
    分析drinks.csv数据文件
    数据字段说明:
    - country: 国家
    - beer_servings: 啤酒消费量
    - spirit_servings: 烈酒消费量
    - wine_servings: 红酒消费量
    - total_litres_of_pure_alchol: 消费的纯酒精统计
    - continent: 大陆
    """
    # 读取CSV文件
    df = pd.read_csv('exercise_data\drinks.csv')

    # 1. 分析哪个大陆平均消耗啤酒更多
    beer_by_continent = df.groupby('continent')['beer_servings'].mean()
    print("\n1. 各大陆平均啤酒消耗量:")
    print(beer_by_continent)
    print(f"\n啤酒消耗最多的大陆是: {beer_by_continent.idxmax()}")

    # 2. 每个大陆的红酒消耗描述性统计
    print("\n2. 各大陆红酒消耗描述性统计:")
    print(df.groupby('continent')['wine_servings'].describe())

    # 3. 每个大陆每种酒类别的平均消耗
    alcohol_columns = ['beer_servings', 'spirit_servings', 'wine_servings']
    print("\n3. 各大陆所有酒类别的平均消耗:")
    print(df.groupby('continent')[alcohol_columns].mean())

    # 4. 每个大陆每种酒类别的消耗中位数
    print("\n4. 各大陆所有酒类别的消耗中位数:")
    print(df.groupby('continent')[alcohol_columns].median())

if __name__ == "__main__":
    analyze_drinks()
