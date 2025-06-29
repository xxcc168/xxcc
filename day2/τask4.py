import numpy as np

# 创建3x4的二维数组
arr = np.arange(1, 13).reshape(3, 4)
print("原始数组：")
print(arr)

# 1. 打印数组的形状、维度和数据类型
print("\n数组属性：")
print(f"形状(shape): {arr.shape}")
print(f"维度(ndim): {arr.ndim}")
print(f"数据类型(dtype): {arr.dtype}")

# 2. 将数组元素乘以2
arr_doubled = arr * 2
print("\n数组元素乘以2后：")
print(arr_doubled)

# 3. 将数组重塑为4x3的形状
arr_reshaped = arr.reshape(4, 3)
print("\n重塑为4x3的数组：")
print(arr_reshaped)
