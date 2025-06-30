import pandas as pd
import os

def analyze_city_data():
    # 设置数据文件路径
    data_path = r'D:\Drivers\pydata\PythonProject1\day3\data'
    files = [
        '2015年国内主要城市年度数据.csv',
        '2016年国内主要城市年度数据.csv',
        '2017年国内主要城市年度数据.csv'
    ]

    # 读取并合并数据
    dfs = []
    for file in files:
        df = pd.read_csv(os.path.join(data_path, file), encoding='utf-8-sig')
        # 从文件名中提取年份
        year = int(file[:4])
        df['年份'] = year
        dfs.append(df)

    # 1. 纵向合并数据
    merged_df = pd.concat(dfs, ignore_index=True)

    # 4. 处理缺省值
    merged_df = merged_df.fillna(0)

    # 2. 按年份聚合
    yearly_data = merged_df.groupby('年份')

    # 3. 计算每年的国内生产总值
    yearly_gdp = yearly_data['国内生产总值'].sum()

    # 输出结果
    print("\n各年份数据概况：")
    print(yearly_data.size())

    print("\n各年份国内生产总值：")
    print(yearly_gdp)

    # 保存合并后的数据
    output_path = os.path.join(data_path, '生产总值.csv')
    merged_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"\n合并数据已保存至: {output_path}")

    # 5. 计算每个城市GDP年均增长率并找出最高/最低的五个城市
    city_growth = merged_df.pivot(index='地区', columns='年份', values='国内生产总值')
    city_growth['年均增长率(%)'] = ((city_growth[2017] / city_growth[2015]) ** (1/2) - 1) * 100
    top5 = city_growth.nlargest(5, '年均增长率(%)')
    bottom5 = city_growth.nsmallest(5, '年均增长率(%)')

    print("\nGDP年均增长率最高的5个城市:")
    print(top5[['年均增长率(%)']])
    print("\nGDP年均增长率最低的5个城市:")
    print(bottom5[['年均增长率(%)']])

    # 6. 对医院、卫生院数进行归一化处理并比较变化
    merged_df['医院数归一化'] = merged_df.groupby('年份')['医院、卫生院数'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min())
    )
    hospital_change = merged_df.pivot_table(index='地区', columns='年份', values='医院数归一化')
    print("\n各城市医院数归一化值变化:")
    print(hospital_change.head())

    # 7. 提取四大城市数据并保存为新CSV
    big4_cities = ['北京', '上海', '广州', '深圳']
    big4_data = merged_df[merged_df['地区'].isin(big4_cities)]
    big4_output = os.path.join(data_path, '四大城市数据.csv')
    big4_data.to_csv(big4_output, index=False, encoding='utf-8-sig')
    print(f"\n四大城市数据已保存至: {big4_output}")

if __name__ == "__main__":
    analyze_city_data()

