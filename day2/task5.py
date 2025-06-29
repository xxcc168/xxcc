import numpy as np

# 创建4x4数组
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

print("原始数组：")
print(array)

# 1. 提取第2行所有元素（索引1）
second_row = array[1]
print("\n第2行所有元素：")
print(second_row)

# 2. 提取第3列所有元素（索引2）
third_column = array[:, 2]
print("\n第3列所有元素：")
print(third_column)

# 3. 提取子数组（第1、2行和第2、3列）
sub_array = array[0:2, 1:3]
print("\n子数组（第1、2行和第2、3列）：")
print(sub_array)

# 4. 将大于10的元素替换为0
array[array > 10] = 0
print("\n将大于10的元素替换为0后的数组：")
print(array)
