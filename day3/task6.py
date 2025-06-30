import pandas as pd
import numpy as np

# 1. 创建包含缺失值的DataFrame
students = pd.DataFrame({
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Score': [85, np.nan, 78, 92, 88],
    'Grade': ['B', 'C', 'C', 'A', 'B']
})

# 保存为students.csv
students.to_csv('d:/Drivers/pydata/PythonProject1/day3/students.csv', index=False)

# 2. 读取CSV文件，打印前3行
students_df = pd.read_csv('d:/Drivers/pydata/PythonProject1/day3/students.csv')
print(students_df.head(3))

# 3. 填充缺失值
mean_score = students_df['Score'].mean()
students_df['Score'] = students_df['Score'].fillna(mean_score)
students_df['Name'] = students_df['Name'].fillna('Unknown')

# 4. 保存为新CSV文件
students_df.to_csv('d:/Drivers/pydata/PythonProject1/day3/students_cleaned.csv', index=False)

